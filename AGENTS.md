# Repository Agent Instructions


## Global Git Top-Level Policy (Mandatory)

- Inherit `ORUDA-GIT-TOP-LEVEL-POLICY v1.0.0` from `babyandi/ORUDA-Master-Queue/governance/ORUDA_GLOBAL_GIT_OPERATING_POLICY_v1.0.0.md`.
- Before work, read the latest target `main`, this `AGENTS.md`, open PRs and relevant Master Queue state; GitHub is the source of truth.
- All changes use: latest `main` → dedicated branch → validation → GitHub read-back → Draft PR.
- Direct `main` writes and automatic merges are prohibited.
- Unverified `DONE`, `PASS`, deployment, Production/Commercial GO, FinalLock, OAsset FinalLock and Final OAudit PASS are prohibited.
- Check overlapping PRs, dependencies, conflicts and protected boundaries before editing.
- On stale base, conflict, missing evidence, failed read-back or boundary violation, fail closed as `HOLD`/`BLOCKED`/`CONFLICT` with an exact reason and resume trigger.
- Scheduled automation inherits the same rules and receives no merge, deployment, GO or FinalLock authority from being enabled.
- Repository-specific rules may strengthen but never weaken this policy.

