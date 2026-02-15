# Canonical hashing (proposal)

This document proposes interoperable canonical hashing rules for decision.forum artifacts.

## Goal
Given the same DecisionRecord payload, all implementations MUST compute the same `record_hash`.

## Recommendation (v0)
Use **RFC 8785 JSON Canonicalization Scheme (JCS)** and hash the canonical UTF-8 bytes with **SHA-256**.

- Canonicalization: https://www.rfc-editor.org/rfc/rfc8785
- Hash: SHA-256 over the canonical JSON bytes

This avoids footguns around key ordering, whitespace, float formatting, and Unicode normalization.

## Hash-churn exclusions
When computing `record_hash`, the canonical payload MUST exclude operationally-mutable fields:
- `record_hash`
- `custody` (CustodyEvent[])
- `anchors` (AnchorReceipt[])
- `created_at`, `updated_at` (if present)
- lifecycle `status` (if present)

Rationale: approvals/attestations must remain valid while custody events and status evolve.

## Optional domain separation
If we later sign or hash multiple object types, add a domain separator:

- `DECISION_FORUM:DecisionRecord:v0:` + canonical-json-bytes

## Open questions
- Do we allow JSON numbers beyond safe integer range? (Recommendation: avoid; use strings for big ints.)
- Do we require a stable timezone format for timestamps? (Recommendation: RFC3339 UTC `Z`.)
