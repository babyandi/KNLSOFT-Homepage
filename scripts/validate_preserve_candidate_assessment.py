#!/usr/bin/env python3
import json
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"governance/KNLSOFT_PRESERVE_CANDIDATE_CONTENT_ASSESSMENT.v1.0.0.json"
def main():
 d=json.loads(P.read_text(encoding="utf-8")); errors=[]; r=d.get("results",[])
 if d.get("state")!="AUTOMATED_STRUCTURE_CHECK_COMPLETE_INDEPENDENT_CONTENT_REVIEW_HOLD": errors.append("STATE_INVALID")
 if len(r)!=48 or d.get("readback_count")!=48: errors.append("COVERAGE_INVALID")
 if any(x.get("readback")!="SUCCESS" for x in r): errors.append("READBACK_FAILURE")
 if any(x.get("assessment") not in {"INDEPENDENT_REVIEW_REQUIRED","REWORK"} for x in r): errors.append("FALSE_CONTENT_PASS")
 if d.get("port_authorized_count")!=0 or any(d.get("protected_boundaries",{}).values()): errors.append("PORT_FAIL_OPEN")
 if len(d.get("not_automatically_validated",[]))<12: errors.append("INDEPENDENT_REVIEW_SCOPE_LOW")
 print(json.dumps({"decision":"PASS_AUTOMATED_STRUCTURE_COVERAGE_CANDIDATE" if not errors else "BLOCK","content_suitability_pass":False,"independent_review_required":True,"port_authorized":False,"errors":errors},indent=2))
 return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
