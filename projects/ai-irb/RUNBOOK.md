# AI-IRB Runbook (v0)

## Inputs
- Evidence bundle id(s)
- Proposed change summary
- Affected surfaces

## Workflow
1) Open IRB case (JSON record) with links to evidence.
2) Run panel crosscheck (multi-model) producing CrosscheckReport + receipts.
3) If converged and within authority: write DecisionRecord + ClearanceCertificate.
4) If not converged or high severity: escalate to Chair with:
   - summary
   - dissent
   - recommended safe next action

## Outputs
- `irb-case` record
- `irb-finding` record (panel output)
- `irb-decision` record (chair ruling)
