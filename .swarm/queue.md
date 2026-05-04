# Queue — argilla (Division Level)

Items are listed in priority order within each section.
Item IDs: `<DIVISION-CODE>-<3-digit-number>` — assigned sequentially, never reused.

---

## Active

## Pending

- [ ] [OD-001] [OPEN] Local docker-compose deployment running with oasis branding
      priority: high | project: infra
      notes: Vendor upstream docker-compose, override defaults (ports, default user, default workspace name → 'oasis').

- [ ] [OD-002] [OPEN] Decide canonical brand name for this fork
      priority: high | project: branding
      notes: Options: oasis-data-labeling, oasis-curate, oasis-annotate. Coordinate with sibling fork naming.

- [ ] [ARGI-001] [OPEN] Adapter to ox-collab-api scaffolded at oasis-extensions/ox_collab_adapter.py
      priority: high | project: integration

- [ ] [OD-003] [OPEN] License compliance audit
      priority: medium | project: legal
      notes: Verify NOTICE file is preserved, copyright headers intact, attribution requirements met.

- [ ] [OD-004] [OPEN] oasis-auth SSO integration spike
      priority: medium | project: integration
      notes: Replace upstream's built-in user system with oasis-auth bearer tokens.
      depends: OD-001

- [ ] [OD-005] [OPEN] LAN-friendly deployment manifests
      priority: medium | project: infra
      notes: docker-compose.lan.yaml — bind to 0.0.0.0, optional reverse proxy, mDNS service advertisement
      depends: OD-001

- [ ] [OD-006] [OPEN] Custom UI: rebrand surface
      priority: medium | project: frontend
      notes: Logo, color scheme, footer attribution. Surface only — no functional UI changes yet.
      depends: OD-002

- [ ] [OD-007] [OPEN] Social collaboration features
      priority: low | project: frontend
      notes: Multi-user comments on examples, @-mentions, activity feed.
      depends: OD-006

- [ ] [OD-008] [OPEN] Production deployment manifests (oasis-cloud)
      priority: low | project: infra
      notes: K8s manifests / Helm chart for oasis-cloud-admin to deploy this stack to a research-client cluster.
      depends: OD-001, OD-004

## Done
