#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FILES={
 "intake":"oruda/website/W00/KNLSOFT_WEBSITE_W00_INTAKE.v0.1.0.json",
 "sources":"oruda/website/W00/KNLSOFT_WEBSITE_W00_SOURCE_REGISTER.v0.1.0.json",
 "decisions":"oruda/website/W00/KNLSOFT_WEBSITE_W00_DECISION_BACKLOG.v0.1.0.json",
 "scenarios":"oruda/website/W00/KNLSOFT_WEBSITE_W00_SCENARIOS.v0.1.0.json",
 "roles":"oruda/website/W00/KNLSOFT_WEBSITE_W00_ROLE_AUTHORITY.v0.1.0.json",
 "binding":"oruda/inheritance/KNLSOFT_HOMEPAGE_WEBSITE_ASSET_BINDING.v0.1.0.json",
}
def load_all():
    return {k:json.loads((ROOT/p).read_text(encoding="utf-8")) for k,p in FILES.items()}
def validate_documents(d):
    errors=[]
    def require(c,m):
        if not c: errors.append(m)
    i,s,b,sc,r,bind=d["intake"],d["sources"],d["decisions"],d["scenarios"],d["roles"],d["binding"]
    require(i.get("stage")=="W00","stage must be W00")
    require(i.get("status")=="PREPARATION_IN_PROGRESS_HOLD","W00 status must remain preparation HOLD")
    gate=i.get("gate",{})
    require(gate.get("exit_gate")=="WG-00-INTAKE-COMPLETE","W00 exit gate invalid")
    require(gate.get("exit_result")=="HOLD","W00 exit must remain HOLD")
    require(gate.get("downstream_stage_completion_allowed") is False,"downstream completion must be false")
    require(len(gate.get("blockers",[]))>=4,"W00 blockers incomplete")
    required={"official KNLSOFT logo and brand guideline","official aTops product specification and approved AI role","official SPACEMON product specification and approved AI role","approved product screenshots or demo access","approved customer cases and measurable outcomes"}
    require(required.issubset({x.get("name") for x in s.get("missing_official_sources",[])}),"official source gaps incomplete")
    require(s.get("conflict_rule")=="HIGHER_PRIORITY_SOURCE_WINS_AND_CONFLICT_REQUIRES_DECISION_LOG","source conflict rule missing")
    require(len(b.get("items",[]))>=10,"decision backlog incomplete")
    require(next(x for x in b.get("items",[]) if x.get("decision_id")=="D-W00-004").get("state")=="APPROVED_BY_USER_INSTRUCTION","authority decision not approved")
    require(all(x.get("state")=="OPEN" for x in b.get("items",[]) if x.get("decision_id")!="D-W00-004"),"other decisions must remain OPEN")
    require(b.get("question_policy")=="ASK_ONLY_WHEN_A_DECISION_BECOMES_THE_NEXT_TRUE_HARD_GATE","question policy invalid")
    classes={x.get("class") for x in sc.get("scenarios",[])}
    require(classes=={"NORMAL","EXCEPTION","RECOVERY"},"normal exception recovery coverage incomplete")
    require(r.get("delegation_spine")==["OBusinessPlanning","OBusinessAdmin","OManager","OProjectManager","OProjectLeader","OBuilder"],"delegation spine invalid")
    require({x.get("role") for x in r.get("actual_role_instances",[])}=={"HUMAN_DECISION_OWNER","OManager"},"control role instances invalid")
    auth={x.get("role"):x for x in r.get("W00_authority",[])}
    require(auth.get("OProjectManager",{}).get("activation")=="NOT_ALLOWED_BEFORE_W00_EXIT","OProjectManager activated too early")
    require(auth.get("OBuilder",{}).get("activation")=="NOT_ALLOWED_BEFORE_APPROVED_BUILD_REQUEST","OBuilder activated too early")
    stages=bind.get("stage_adoption",{})
    require(stages.get("W00")=="PREPARATION_IN_PROGRESS_HOLD","binding W00 state invalid")
    require(all(stages.get(f"W{x:02d}")=="CANDIDATE_PREPARATION_HOLD" for x in range(1,8)),"W01-W07 may only be candidate preparation")
    require(stages.get("W08")=="ENTRY_PREPARATION_HOLD" and all(stages.get(f"W{x:02d}")=="NOT_ASSESSED" for x in range(9,15)),"W08 entry/W09-W14 state invalid")
    ex=i.get("execution_boundary",{})
    for flag in ["W01_completed","wireframe_allowed","visual_design_allowed","implementation_allowed","production_go","commercial_go","final_lock"]:
        require(ex.get(flag) is False,f"{flag} must remain false")
    return errors
def main():
    errors=validate_documents(load_all())
    if errors:
        for e in errors: print(f"[FAIL] {e}")
        return 1
    print("PASS_KNLSOFT_W00_PREPARATION_WITH_EXIT_HOLD")
    return 0
if __name__=="__main__": sys.exit(main())
