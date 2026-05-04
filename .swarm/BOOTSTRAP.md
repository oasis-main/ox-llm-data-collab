# .swarm Bootstrap

Anyone (human or agent) entering this repo: read all 5 files in this directory in order before acting.

1. **BOOTSTRAP.md** (this file) — orientation
2. **context.md** — what this project is and what makes it different
3. **state.md** — current snapshot: what's done, what's blocked, what's next
4. **queue.md** — work items, append-only IDs, priority + dependencies
5. **memory.md** — append-only decisions, gotchas, design rationale

Protocol: dot_swarm (https://github.com/oasis-main/dot_swarm). Markdown-native, environment-first, async-coordination via filesystem.

## Conventions
- Item IDs are sequential `<PREFIX>-<NNN>`, never reused, never renumbered.
- `state.md` is overwritten on every update; `memory.md` and `queue.md`'s Done section are append-only.
- New decisions or non-obvious findings → memory.md (with date).
- Status emoji in queue: `[ ]` open, `[>]` active, `[x]` done, `[!]` blocked.
