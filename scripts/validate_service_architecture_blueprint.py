#!/usr/bin/env python3
import json
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "docs/31_KNLSOFT_SERVICE_ARCHITECTURE_BLUEPRINT.v1.0.0.json"

def main():
    d = json.loads(P.read_text(encoding="utf-8"))
    errors = []
    if d.get("state") != "PRE_GO_SPECIFICATION_CANDIDATE": errors.append("STATE_INVALID")
    if len(d.get("users_and_decisions", [])) < 6: errors.append("ROLE_COVERAGE_LOW")
    types = {x.get("type") for x in d.get("scenarios", [])}
    if types != {"NORMAL","EXCEPTION","RECOVERY"}: errors.append("SCENARIO_TYPE_COVERAGE_INVALID")
    if len(d.get("functional_architecture", [])) < 5: errors.append("FUNCTIONAL_DOMAIN_COVERAGE_LOW")
    if len(d.get("sitemap", [])) < 10: errors.append("SITEMAP_COVERAGE_LOW")
    gates = d.get("gates", {})
    if gates.get("visual_design_gate") != "BLOCKED" or gates.get("implementation_gate") != "BLOCKED" or gates.get("formal_go") is not False: errors.append("PRE_GO_FAIL_OPEN")
    if "AI_OWNER_AND_EVIDENCE_APPROVER" != d.get("ai_contract", {}).get("publication_gate"): errors.append("AI_GATE_INVALID")
    required_states = {"EMPTY","EDITING","INVALID","READY","SUBMITTING","RECEIVED","ROUTING","ASSIGNED","FAILED_RECOVERABLE","CLOSED"}
    if set(d.get("task_states", {}).get("inquiry", [])) != required_states: errors.append("INQUIRY_STATE_MODEL_INVALID")
    print(json.dumps({"validator":"validate_blueprint.py","decision":"PASS_PRE_GO_SERVICE_ARCHITECTURE_CANDIDATE" if not errors else "BLOCK","formal_go":False,"visual_design":False,"implementation":False,"errors":errors}, indent=2))
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())
