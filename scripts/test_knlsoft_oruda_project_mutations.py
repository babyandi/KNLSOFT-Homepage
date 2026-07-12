#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts/validate_knlsoft_oruda_project.py"


def module():
    spec = importlib.util.spec_from_file_location("knlsoft_oruda_validator", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("VALIDATOR_LOAD_FAILED")
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


v = module()
project = v.load(v.PROJECT_PATH)
artifact = v.load(v.ARTIFACT_PATH)
ledger = v.load(v.GATE_PATH)


def case(target: str, mutate: Callable[[dict[str, Any]], None], expected: str) -> bool:
    p, a, g = copy.deepcopy(project), copy.deepcopy(artifact), copy.deepcopy(ledger)
    mutate({"project": p, "artifact": a, "ledger": g}[target])
    return expected in v.validate_documents(p, a, g)


def main() -> int:
    cases = {
        "entry_bypass": case(
            "project", lambda x: x["entry_program"].update(bypass_allowed=True), "ENTRY_GATE_FAIL_OPEN"
        ),
        "runtime_claim": case(
            "project",
            lambda x: x["execution_boundary"].update(actual_oruda_runtime_execution=True),
            "EXECUTION_BOUNDARY_FAIL_OPEN",
        ),
        "input_promoted": case(
            "project",
            lambda x: x["input_documents"].update(official_oruda_output=True),
            "INPUT_FALSELY_PROMOTED_TO_ORUDA_OUTPUT",
        ),
        "project_manager_false_pass": case(
            "artifact", lambda x: x["stages"][6].update(state="PASS"), "DOWNSTREAM_STAGE_FALSE_PASS"
        ),
        "view_removed": case(
            "artifact", lambda x: x["required_assurance_chain"].remove("OView"), "ASSURANCE_CHAIN_INVALID"
        ),
        "obp_gate_opened": case(
            "ledger", lambda x: next(g for g in x["gates"] if g["gate"] == "OBP-ENTRY").update(result="PASS"), "OBP_GATE_LEDGER_FAIL_OPEN"
        ),
        "w00_gate_opened": case(
            "ledger", lambda x: next(g for g in x["gates"] if g["gate"] == "WG-00").update(result="PASS"), "W00_GATE_LEDGER_FAIL_OPEN"
        ),
        "direct_builder_request": case(
            "artifact",
            lambda x: x.update(obuilder_intake_rule="DIRECT_BUSINESS_REQUEST_ALLOWED"),
            "OBUILDER_DIRECT_REQUEST_FAIL_OPEN",
        ),
    }
    failed = [name for name, passed in cases.items() if not passed]
    print(
        json.dumps(
            {
                "harness": "test_knlsoft_oruda_project_mutations.py",
                "decision": "PASS" if not failed else "BLOCK",
                "cases": len(cases),
                "failed": failed,
                "oruda_runtime_execution": False,
                "production_go": False,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
