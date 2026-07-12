#!/usr/bin/env python3
import json
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "docs/32_KNLSOFT_CONTENT_EVIDENCE_WIREFRAME_SPEC.v1.0.0.json"

def main():
    d = json.loads(P.read_text(encoding="utf-8"))
    errors = []
    if d.get("state") != "LOW_FIDELITY_SPECIFICATION_CANDIDATE": errors.append("STATE_INVALID")
    statuses = set(d.get("content_status_model", []))
    if statuses != {"OFFICIAL","VERIFIED","CANDIDATE","CONCEPT","MISSING","WITHDRAWN"}: errors.append("CONTENT_STATUS_INVALID")
    matrix = d.get("claim_data_evidence_matrix", [])
    if len(matrix) < 8: errors.append("CLAIM_COVERAGE_LOW")
    if any(not x.get("data_required") or not x.get("evidence_required") or not x.get("owner") for x in matrix): errors.append("CLAIM_CONTROL_INCOMPLETE")
    pages = d.get("page_wireframes", [])
    if len(pages) < 4: errors.append("REPRESENTATIVE_PAGE_COVERAGE_LOW")
    for page in pages:
        orders = [x.get("order") for x in page.get("sections", [])]
        if orders != list(range(1, len(orders) + 1)): errors.append("SECTION_ORDER_INVALID:" + page.get("page",""))
        for section in page.get("sections", []):
            for key in ["purpose","content","evidence","layout","primary_action","fallback"]:
                if not section.get(key): errors.append("SECTION_CONTRACT_MISSING:" + section.get("id","") + ":" + key)
    if len(d.get("test_oracles", [])) < 8: errors.append("TEST_ORACLE_COVERAGE_LOW")
    gate = d.get("gate_result", {})
    if gate.get("low_fidelity_wireframe") != "PASS_CANDIDATE": errors.append("WIREFRAME_GATE_INVALID")
    if gate.get("representative_screen_visual_design") != "BLOCKED" or gate.get("implementation") != "BLOCKED" or gate.get("formal_go") is not False: errors.append("DOWNSTREAM_FAIL_OPEN")
    print(json.dumps({"validator":"validate_content_wireframe.py","decision":"PASS_LOW_FIDELITY_WIREFRAME_CANDIDATE" if not errors else "BLOCK","content_evidence_gate":"HOLD","visual_design":False,"implementation":False,"errors":errors}, indent=2))
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())
