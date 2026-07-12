# KNLSOFT Homepage — ORUDA Website Program Asset Inheritance

Status: **Upstream Draft Candidate Pinned**

KNLSOFT Homepage references ORUDA PR #23 commit `102b84c091e132cf965c4f47e3c0daa5d617bb2a`.

- Profile A Content is primary.
- Profile E AI applies to aTops and SPACEMON positioning, but AI claims remain inactive until verified evidence exists.
- Profile C Workflow applies only to inquiry, demo and future CMS/admin workflows.
- Common W00–W14 processes, rules, templates and validators are not copied into this repository.
- Previous strategy documents remain `ORUDA_INTAKE_INPUT_CANDIDATE`.
- W00–W14 remain `NOT_ASSESSED`; design and implementation do not receive retroactive PASS.
- UI, CSS, implementation, test execution, deployment and GO states remain unchanged.

## RCA — CI workflow insertion no-op

- **Failure:** the first workflow update matched escaped newline text instead of actual line breaks, producing a commit with unchanged file content.
- **Detection:** the returned content SHA was unchanged.
- **Correction:** re-read the branch file, required an exact multiline insertion anchor, and verified a new content SHA.
- **Prevention:** future workflow edits must fail when the insertion anchor is absent and must compare content SHA before reporting application.
