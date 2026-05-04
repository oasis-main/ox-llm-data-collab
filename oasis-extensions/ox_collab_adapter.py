"""Adapter: argilla examples → ox-collab-api records.

Pulls examples from argilla's `/api/v1/datasets/{id}/records` endpoint and POSTs them
as records to ox-collab-api. Idempotent — ox-collab-api dedupes on (source, source_id).

Usage:
    python -m oasis-extensions.ox_collab_adapter \\
        --argilla-url http://localhost:6900 \\
        --argilla-key admin.apikey \\
        --collab-url http://localhost:8001 \\
        --dataset my-dataset
"""

from __future__ import annotations

import argparse
import sys
from typing import Any

import httpx


def fetch_argilla_records(
    base: str, api_key: str, dataset_id: str, page_size: int = 100
) -> list[dict[str, Any]]:
    """Fetch all records from an argilla dataset. Yields the raw upstream JSON."""
    headers = {"X-Argilla-Api-Key": api_key}
    out: list[dict[str, Any]] = []
    offset = 0
    with httpx.Client(timeout=30.0) as client:
        while True:
            r = client.get(
                f"{base}/api/v1/datasets/{dataset_id}/records",
                headers=headers,
                params={"limit": page_size, "offset": offset, "include": "responses,suggestions"},
            )
            r.raise_for_status()
            page = r.json().get("items", [])
            if not page:
                break
            out.extend(page)
            offset += len(page)
            if len(page) < page_size:
                break
    return out


def to_collab_record(argilla_record: dict[str, Any], dataset_id: str) -> dict[str, Any]:
    """Map an argilla record into ox-collab-api's Record schema."""
    fields = argilla_record.get("fields", {})
    title = next(iter(fields.values())) if fields else f"record-{argilla_record.get('id')}"
    if isinstance(title, dict):
        title = title.get("value") or str(title)
    body = "\n\n".join(f"**{k}**\n\n{v}" for k, v in fields.items())

    return {
        "source": "argilla",
        "source_id": f"{dataset_id}/{argilla_record.get('id')}",
        "title": str(title)[:255],
        "body": body,
        "extra": {
            "dataset_id": dataset_id,
            "argilla_id": argilla_record.get("id"),
            "responses": argilla_record.get("responses", []),
            "suggestions": argilla_record.get("suggestions", []),
            "metadata": argilla_record.get("metadata", {}),
        },
    }


def push_to_collab(records: list[dict[str, Any]], collab_url: str) -> tuple[int, int]:
    """POST each record to ox-collab-api. Returns (created, skipped)."""
    created = skipped = 0
    with httpx.Client(timeout=30.0, base_url=collab_url) as client:
        for rec in records:
            r = client.post("/records", json=rec, headers={"X-Anon-Name": "argilla-adapter"})
            if r.status_code == 201:
                created += 1
            elif r.status_code == 200:
                skipped += 1
            else:
                print(f"[warn] {r.status_code} for {rec['source_id']}: {r.text[:200]}", file=sys.stderr)
    return created, skipped


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--argilla-url", required=True)
    ap.add_argument("--argilla-key", required=True)
    ap.add_argument("--collab-url", required=True)
    ap.add_argument("--dataset", required=True, help="argilla dataset id")
    args = ap.parse_args()

    print(f"[fetch] {args.argilla_url}/datasets/{args.dataset}")
    raw = fetch_argilla_records(args.argilla_url, args.argilla_key, args.dataset)
    print(f"[fetch] {len(raw)} records")

    mapped = [to_collab_record(r, args.dataset) for r in raw]
    created, skipped = push_to_collab(mapped, args.collab_url)
    print(f"[done] created={created} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
