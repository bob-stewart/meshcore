# AI-IRB Policy (v0)

Goal: ensure changes are **defensible from genesis** with repeatable, evidence-backed review.

## Non-negotiables
- No public network exposure by default.
- No silent privilege escalation.
- No irreversible data deletion without human approval.
- Every consequential change MUST have:
  - Evidence bundle
  - MeshCORE evidence manifest
  - DecisionRecord (or IRB case) if it touches a gateable surface

## Gateable surfaces (v0)
A change MUST be gated by a cleared DecisionRecord (or open IRB case) when it affects:
- Tool permissions / exec allowlists / capability expansions
- Secrets handling / key resolution / auth
- Network exposure (bind address, firewall rules, public endpoints)
- Deployment of long-running services (staging/prod)
- Memory writes to high-trust SoftShell layers
- Governance policy / clearance policy / quorum rules

## Escalation ladder
- Sentinel detects issue → open IRB case.
- IRB panel attempts consensus.
- If consensus is not reached OR severity >= HIGH → escalate to Chair (Bob).

## Quorum defaults
- dev/test: quorum=2
- staging/prod: quorum=3

## Definitions
- "Evidence" = immutable bundle created by HardShell.
- "Manifest" = MeshCORE pointer + metadata.
