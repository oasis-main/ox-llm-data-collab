# argilla (oasis fork) — Memory (append-only)

---

**2026-05-04** — Fork initialized at oasis-main/argilla
Forked from argilla-io/argilla (Apache-2.0). Default branch `develop`. Reason for fork: oasis-data cloud product line — custom branding, better social collaboration, tighter integration with Oasis ecosystem (oasis-auth, oasis-cloud, oasis-dashboard).

License: upstream permissive (verified Apache-2.0 / MIT respectively for argilla / ydata family). License permits SaaS hosting and rebranding; trademark requires we use "oasis-data" naming, not the upstream project name, in our product surface.

Coordinate with sibling fork (oasis-main/argilla ↔ oasis-main/fg-data-profiling) on shared OD-* item IDs.

**2026-05-04** — Why this and not a from-scratch build
Both upstreams have years of UX work, ecosystem integrations, and battle-tested edge cases. Forking the leader and rebranding is dramatically faster than building from scratch, and the permissive licenses make the legal path clean. Risk: upstream churn — mitigated by rebasing weekly off develop and keeping oasis-specific code in well-isolated modules.

**2026-05-04** — Repo renamed from oasis-main/argilla → oasis-main/ox-llm-data-collab
Name reflects product identity: "ox" = oasis-x, "llm" = LLM-data focus, "collab" = collaboration-first UX.
Local remote updated to match.
