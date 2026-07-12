#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PROJECT_PATH = ROOT / "oruda/project/KNLSOFT_WEBSITE_PROJECT.v1.0.0.json"
ARTIFACT_PATH = ROOT / "oruda/project/KNLSOFT_WEBSITE_ARTIFACT_MAP.v1.0.0.json"
GATE_PATH = ROOT / "oruda/project/KNLSOFT_WEBSITE_GATE_LEDGER.v1.0.0.json"

EXPECTED_STAGES = [f"S{i:02d}" for i in range(16)]
EXPECTED_ASSURANCE = ["OTester", "OView", "OAudit", "OAsset"]
EXPECTED_MISSING = {
    "OBusinessPlanning", "OBusinessAdmin", "ORFP", "OAcceptance",
    "OProjectManager", "OProjectLeader", "OVisual",
}
EXPECTED_DELEGATION = [
    "OBusinessPlanning", "OBusinessAdmin", "OManager",
    "OProjectManager", "OProjectLeader", "OBuilder",
]
EXPECTED_TEAMS = {f"OBT-{i:02d}" for i in range(1, 11)}
FORBIDDEN_DOWNSTREAM_PASS_STAGES = {f"S{i:02d}" for i in range(1, 16)}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_documents(
    project: dict[str, Any], artifact: dict[str, Any], ledger: dict[str, Any]
) -> list[str]:
    errors: list[str] = []

    if project.get("state") != "ORUDA_NATIVE_W00_PREPARATION_IN_PROGRESS_ENTRY_GATE_HOLD":
        errors.append("PROJECT_STATE_FAIL_OPEN")

    baseline = project.get("oruda_baseline", {})
    sha = str(baseline.get("commit_sha", ""))
    if len(sha) != 40 or baseline.get("repository") != "babyandi/ORUDA":
        errors.append("ORUDA_BASELINE_NOT_PINNED")

    entry = project.get("entry_program", {})
    if entry.get("program_name") != "OBusinessPlanning":
        errors.append("ENTRY_PROGRAM_INVALID")
    if entry.get("repository_binding_state") != "CANDIDATE_IN_ORUDA_PR_25_NOT_MAIN":
        errors.append("ENTRY_ROLE_BINDING_STATE_INVALID")
    candidate = entry.get("candidate_binding", {})
    if candidate.get("commit_sha") != "ef87184b21b48f0fd994c9f99b63a6422dff8fca" or candidate.get("ci") != "SUCCESS":
        errors.append("ENTRY_ROLE_BINDING_EVIDENCE_INVALID")
    if entry.get("decision") != "BLOCK" or entry.get("bypass_allowed") is not False:
        errors.append("ENTRY_GATE_FAIL_OPEN")

    missing = {item.get("name") for item in project.get("missing_dependencies", [])}
    if missing != EXPECTED_MISSING:
        errors.append("MISSING_DEPENDENCY_SET_INVALID")

    if project.get("delegation_spine") != EXPECTED_DELEGATION:
        errors.append("DELEGATION_SPINE_INVALID")
    separation = project.get("role_separation", {})
    if not separation or any(value is not False for value in separation.values()):
        errors.append("ROLE_SEPARATION_FAIL_OPEN")

    inputs = project.get("input_documents", {})
    if inputs.get("classification") != "ORUDA_INTAKE_INPUT_CANDIDATE":
        errors.append("INPUT_CLASSIFICATION_INVALID")
    if inputs.get("official_oruda_output") is not False:
        errors.append("INPUT_FALSELY_PROMOTED_TO_ORUDA_OUTPUT")

    boundary = project.get("execution_boundary", {})
    if not boundary or any(value is not False for value in boundary.values()):
        errors.append("EXECUTION_BOUNDARY_FAIL_OPEN")

    stages = artifact.get("stages", [])
    stage_ids = [item.get("stage") for item in stages]
    if stage_ids != EXPECTED_STAGES:
        errors.append("STAGE_SEQUENCE_INVALID")
    by_stage = {item.get("stage"): item for item in stages}
    if by_stage.get("S01", {}).get("owner") != "OBusinessPlanning":
        errors.append("OBUSINESSPLANNING_OWNER_MISSING")
    if by_stage.get("S01", {}).get("state") != "BLOCKED":
        errors.append("OBP_STAGE_FAIL_OPEN")
    if by_stage.get("S06", {}).get("owner") != "OProjectManager":
        errors.append("OPROJECTMANAGER_OWNER_MISSING")
    if by_stage.get("S07", {}).get("owner") != "OProjectLeader":
        errors.append("OPROJECTLEADER_OWNER_MISSING")
    if by_stage.get("S09", {}).get("owner") != "OBuilder.InternalTeams":
        errors.append("OBUILDER_TEAM_OWNER_MISSING")
    if any(
        by_stage.get(stage, {}).get("state", "").startswith("PASS")
        for stage in FORBIDDEN_DOWNSTREAM_PASS_STAGES
    ):
        errors.append("DOWNSTREAM_STAGE_FALSE_PASS")

    if artifact.get("required_assurance_chain") != EXPECTED_ASSURANCE:
        errors.append("ASSURANCE_CHAIN_INVALID")
    teams = artifact.get("obuilder_team_directory", [])
    team_ids = {item.get("team_id") for item in teams}
    if team_ids != EXPECTED_TEAMS:
        errors.append("OBUILDER_TEAM_DIRECTORY_INVALID")
    if artifact.get("obuilder_intake_rule") != "ONLY_OPROJECTLEADER_BUILD_REQUEST_PACKAGE_ACCEPTED":
        errors.append("OBUILDER_DIRECT_REQUEST_FAIL_OPEN")
    required_rules = {
        "NO_PASS_WITHOUT_OVIEW_INDEPENDENT_VERIFICATION",
        "NO_APPROVAL_WITHOUT_OAUDIT_EVIDENCE",
        "NO_REUSE_BASELINE_WITHOUT_OASSET_IDENTITY_AND_PROVENANCE",
    }
    if not required_rules.issubset(set(artifact.get("promotion_rules", []))):
        errors.append("PROMOTION_GUARD_MISSING")

    gates = {item.get("gate"): item for item in ledger.get("gates", [])}
    if ledger.get("state") != "W00_PREPARATION_PASS_CONTROL_CANDIDATE_EXIT_HOLD":
        errors.append("GATE_LEDGER_STATE_INVALID")
    if gates.get("OBP-ENTRY", {}).get("result") != "BLOCK":
        errors.append("OBP_GATE_LEDGER_FAIL_OPEN")
    if gates.get("WG-00", {}).get("result") != "HOLD":
        errors.append("W00_GATE_LEDGER_FAIL_OPEN")
    if ledger.get("true_hard_gate") != "WG-00":
        errors.append("TRUE_HARD_GATE_INVALID")
    if ledger.get("downstream_pass_allowed") is not False:
        errors.append("DOWNSTREAM_PROMOTION_FAIL_OPEN")

    return errors


def validate() -> list[str]:
    missing = [path for path in (PROJECT_PATH, ARTIFACT_PATH, GATE_PATH) if not path.is_file()]
    if missing:
        return [f"MISSING:{path.relative_to(ROOT)}" for path in missing]
    return validate_documents(load(PROJECT_PATH), load(ARTIFACT_PATH), load(GATE_PATH))


def main() -> int:
    try:
        errors = validate()
    except Exception as exc:
        errors = [f"VALIDATION_EXCEPTION:{type(exc).__name__}:{exc}"]
    result = {
        "validator": "validate_knlsoft_oruda_project.py",
        "decision": "PASS_CONTROL_STRUCTURE_WITH_W00_EXIT_HOLD" if not errors else "BLOCK",
        "oruda_runtime_execution": False,
        "website_implementation": False,
        "actual_test_execution": False,
        "production_go": False,
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
