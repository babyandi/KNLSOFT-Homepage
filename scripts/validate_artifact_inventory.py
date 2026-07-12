#!/usr/bin/env python3
import json
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"governance/KNLSOFT_TAILORED_MASTER_ARTIFACT_INVENTORY.v1.0.0.json"
def main():
 d=json.loads(P.read_text(encoding="utf-8")); errors=[]; e=d.get("entries",[])
 if d.get("state")!="INVENTORY_CLASSIFIED_CONTENT_VALIDATION_HOLD": errors.append("STATE_INVALID")
 if len(e)!=89 or d.get("inventory_count")!=89: errors.append("INVENTORY_COUNT_INVALID")
 if len({x.get("artifact_id") for x in e})!=89 or len({x.get("source_path") for x in e})!=89: errors.append("IDENTITY_DUPLICATE")
 if sum(d.get("disposition_counts",{}).values())!=89: errors.append("DISPOSITION_COUNT_INVALID")
 allowed={"PRESERVE_CANDIDATE","REVALIDATE_ON_LATEST_MAIN","QUARANTINE_REJECTED_BASELINE","BLOCKED_EXTERNAL_EVIDENCE"}
 if {x.get("disposition") for x in e}!=allowed: errors.append("DISPOSITION_SET_INVALID")
 if any(x.get("content_validation")!="NOT_EXECUTED" or x.get("port_authorized") is not False for x in e): errors.append("PORT_FAIL_OPEN")
 if any(d.get("protected_boundaries",{}).values()): errors.append("BOUNDARY_FAIL_OPEN")
 if d.get("source_count_reconciliation",{}).get("difference")!=3: errors.append("COUNT_RCA_MISSING")
 print(json.dumps({"decision":"PASS_ARTIFACT_INVENTORY_CLASSIFICATION_CANDIDATE" if not errors else "BLOCK","inventory_count":len(e),"content_validation_executed":False,"port_authorized":False,"errors":errors},indent=2))
 return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
