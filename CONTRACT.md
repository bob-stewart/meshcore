# MeshCORE Contract (v0)

MeshCORE is an agent-agnostic continuity layer.

## Non-negotiables

1) **Decisions are append-only**
- Human-level intent must be recorded as short, dated entries.

2) **State is machine-readable**
- Canonical state lives in `state/mesh.json`.

3) **Evidence is immutable**
- Evidence bundles are timestamped and never edited in place.
- MeshCORE stores pointers/manifests; external systems (e.g., HardShell) may generate the bundles.

## Directory layout

- `decisions/` — append-only decision ledger
- `state/` — canonical structured state
- `evidence/` — manifests + pointers (not necessarily the full bundle contents)
- `softshell/` — durable agentic memory notes (curated)
- `schemas/` — JSON Schemas for records/manifests

## Record schemas (initial)

- Decision record: `schemas/decision.schema.json`
- State: `schemas/state.schema.json`
- Evidence manifest: `schemas/evidence.schema.json`
