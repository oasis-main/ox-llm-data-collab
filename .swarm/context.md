# argilla (oasis fork) — Context

## What this is
Fork of argilla-io/argilla (Apache-2.0), maintained at oasis-main/argilla.

## Why we forked
Argilla is the leading open-source labeling/curation tool for AI data. We fork to (a) integrate with Oasis ecosystem auth/storage, (b) layer on a custom-branded UI with stronger social collaboration features (multi-user review threads, @-mentions, activity feeds), and (c) ship as a turnkey product for research clients via oasis-cloud.

## Strategic position
Part of the **oasis-data** cloud product line. Sibling forks:
- oasis-main/argilla — interactive labeling / curation UI
- oasis-main/fg-data-profiling — automated profiling / EDA

Both rebrand under the oasis-data umbrella with custom UI, better social collaboration features, and tighter integration with the rest of the Oasis ecosystem (oasis-auth, oasis-cloud, oasis-dashboard).

## Deployment trajectory (per oasis-claw pattern)
1. Local container (docker-compose) — running on dev laptops + LAN
2. LAN collaboration — multiple researchers pointing at one shared instance
3. Production — research-client deployments + public SaaS via oasis-cloud

## License posture
Upstream is permissive (Apache-2.0 / MIT). Fork retains upstream license for shared code; new oasis-specific modules are dual-licensed Apache-2.0 + commercial. Trademark: "oasis-data" branding in our distribution; preserve upstream NOTICE/copyright for redistributed code.

## Key upstream branches to track
- `develop` — upstream's active branch (our default)
- `main` — upstream's release branch
We rebase oasis-* feature branches off upstream develop weekly.
