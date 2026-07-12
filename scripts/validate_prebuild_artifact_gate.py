#!/usr/bin/env python3
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "docs/33_KNLSOFT_PREBUILD_ARTIFACT_ASSURANCE_GATE.v1.0.0.json"
def main():
    d=json.loads(P.read_text(encoding="utf-8")); errors=[]
    if d.get("state")!="HOLD_ARTIFACT_VALIDATION_NOT_EXECUTED": errors.append("STATE_FAIL_OPEN")
    if len(d.get("required_validation_packages",[]))!=12: errors.append("VALIDATION_PACKAGE_COUNT_INVALID")
    if set(d.get("required_assurance_roles",[]))!={"OProjectManager","OProjectLeader","OTester","OView","OAudit","OAsset","OManager"}: errors.append("ROLE_COVERAGE_INVALID")
    if any(d.get("current_state",{}).values()): errors.append("PREBUILD_STATE_FAIL_OPEN")
    for x in ["OPROJECTLEADER_BUILD_REQUEST","OBUILDER_IMPLEMENTATION","PRODUCTION_DEPLOYMENT"]:
        if x not in d.get("prohibited_work",[]): errors.append("PROHIBITION_MISSING:"+x)
    print(json.dumps({"decision":"PASS_KNLSOFT_PREBUILD_HOLD_CONTROL" if not errors else "BLOCK","artifact_validation_executed":False,"prebuild_go":False,"errors":errors},indent=2))
    return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
