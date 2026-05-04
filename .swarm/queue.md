# argilla (oasis fork) — Queue

Item IDs: `OD-<3-digit-number>` shared across the oasis-data fork family. Check sibling repos before assigning a new ID.

---

## Active

(no active items)

---

## Pending

- [ ] [OD-001] [OPEN] Local docker-compose deployment running with oasis branding
      priority: high | project: infra
      notes: Vendor upstream docker-compose, override defaults (ports, default user, default workspace name → 'oasis').
             Verify clean startup. Document in README-OASIS.md.

- [ ] [OD-002] [OPEN] Decide canonical brand name for this fork
      priority: high | project: branding
      notes: Options: oasis-data-labeling, oasis-curate, oasis-annotate. Coordinate with sibling fork naming.
             Update repo description + topics on GitHub once decided.

- [ ] [OD-003] [OPEN] License compliance audit
      priority: medium | project: legal
      notes: Verify NOTICE file is preserved, copyright headers intact, attribution requirements met.
             Document license posture in README-OASIS.md.

- [ ] [OD-004] [OPEN] oasis-auth SSO integration spike
      priority: medium | project: integration
      depends: OD-001
      notes: Replace upstream's built-in user system with oasis-auth bearer tokens.
             Spike branch only; do not merge to develop until reviewed.

- [ ] [OD-005] [OPEN] LAN-friendly deployment manifests
      priority: medium | project: infra
      depends: OD-001
      notes: docker-compose.lan.yaml — bind to 0.0.0.0, optional reverse proxy, mDNS service advertisement
             (similar to oasis-claw LAN pattern).

- [ ] [OD-006] [OPEN] Custom UI: rebrand surface
      priority: medium | project: frontend
      depends: OD-002
      notes: Logo, color scheme, footer attribution. Surface only — no functional UI changes yet.

- [ ] [OD-007] [OPEN] Social collaboration features
      priority: low | project: frontend
      depends: OD-006
      notes: Multi-user comments on examples, @-mentions, activity feed.
             Out of scope until baseline rebrand and SSO are done.

- [ ] [OD-008] [OPEN] Production deployment manifests (oasis-cloud)
      priority: low | project: infra
      depends: OD-001, OD-004
      notes: K8s manifests / Helm chart for oasis-cloud-admin to deploy this stack to a research-client cluster.

---

## Done

(none yet)
