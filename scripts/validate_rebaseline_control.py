#!/usr/bin/env python3
import json
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "governance/KNLSOFT_REBASELINE_CONTROL.v1.0.0.json"

def main():
    d=json.loads(P.read_text(encoding="utf-8")); errors=[]
    if d.get("state")!="REBASELINE_ANALYZED_HOLD": errors.append("STATE_INVALID")
    old=d.get("legacy_draft",{})
    if old.get("mergeable") is not False or old.get("disposition")!="CONFLICT_HOLD_NO_FURTHER_WRITES": errors.append("STALE_PR_FAIL_OPEN")
    if old.get("changed_file_count")!=92 or old.get("behind_by")!=1: errors.append("COMPARE_EVIDENCE_DRIFT")
    if len(d.get("upstream_dependencies",[]))<4: errors.append("DEPENDENCY_COVERAGE_LOW")
    if len(d.get("reconciliation_classes",[]))!=5: errors.append("RECONCILIATION_CLASS_INVALID")
    if len(d.get("artifact_work_order",[]))!=8: errors.append("WORK_ORDER_INVALID")
    if any(d.get("protected_boundaries",{}).values()): errors.append("PROTECTED_BOUNDARY_FAIL_OPEN")
    if d.get("master_queue",{}).get("gq1_to_gq8")!="REGISTERED_NOT_EXECUTED": errors.append("QUEUE_FALSE_EXECUTION")
    print(json.dumps({"decision":"PASS_REBASELINE_CONTROL_CANDIDATE" if not errors else "BLOCK","legacy_pr":"CONFLICT_HOLD","artifact_port_executed":False,"implementation":False,"errors":errors},indent=2))
    return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
