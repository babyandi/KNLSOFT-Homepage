#!/usr/bin/env python3
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={
 "purpose":"oruda/website/W01/KNLSOFT_WEBSITE_W01_PURPOSE_OUTCOME.v0.1.0.json",
 "measures":"oruda/website/W01/KNLSOFT_WEBSITE_W01_MEASURE_REGISTRY.v0.1.0.json",
 "users":"oruda/website/W02/KNLSOFT_WEBSITE_W02_USER_ROLE_CONTEXT.v0.1.0.json",
 "buying":"oruda/website/W02/KNLSOFT_WEBSITE_W02_BUYING_DECISION_FLOW.v0.1.0.json",
 "binding":"oruda/inheritance/KNLSOFT_HOMEPAGE_WEBSITE_ASSET_BINDING.v0.1.0.json"}
def load_all(): return {k:json.loads((ROOT/v).read_text(encoding="utf-8")) for k,v in P.items()}
def validate_documents(d):
 e=[]
 req=lambda c,m:e.append(m) if not c else None
 p,m,u,b,bind=d["purpose"],d["measures"],d["users"],d["buying"],d["binding"]
 req(p.get("status")=="CANDIDATE_PREPARATION_HOLD","W01 status invalid")
 req(p.get("entry_dependency",{}).get("formal_W01_execution_allowed") is False,"formal W01 execution opened")
 req(p.get("exit_gate",{}).get("result")=="HOLD","WG-01 must remain HOLD")
 req(len(p.get("business_outcome_candidates",[]))>=6,"outcome coverage incomplete")
 req(all(x.get("status")=="HYPOTHESIS" for x in p.get("business_outcome_candidates",[])),"outcomes falsely approved")
 req(m.get("status")=="DRAFT_NO_NUMERIC_TARGETS","measure status invalid")
 req(all(x.get("target") in ["DECISION_REQUIRED","NO_UNVERIFIED_FACTS","POLICY_DEFINED_BEFORE_W12","BUDGET_REQUIRED_BEFORE_W10"] for x in m.get("measures",[])),"invented numeric target detected")
 req(u.get("status")=="CANDIDATE_PREPARATION_HOLD","W02 status invalid")
 req(u.get("entry_dependency",{}).get("formal_W02_execution_allowed") is False,"formal W02 execution opened")
 req(u.get("exit_gate",{}).get("result")=="HOLD","WG-02 must remain HOLD")
 req(len(u.get("user_groups",[]))>=7,"user coverage incomplete")
 req(all(x.get("evidence_status")!="VERIFIED" for x in u.get("user_groups",[])),"user hypothesis falsely verified")
 roles={x.get("role_id") for x in b.get("decision_roles",[])}
 req(roles=={f"BR-0{i}" for i in range(1,8)},"buying decision roles incomplete")
 req(len(b.get("exceptions",[]))>=4,"buying flow exception recovery incomplete")
 stages=bind.get("stage_adoption",{})
 req(stages.get("W00")=="PREPARATION_IN_PROGRESS_HOLD","W00 binding state invalid")
 req(stages.get("W01")=="CANDIDATE_PREPARATION_HOLD","W01 binding state invalid")
 req(stages.get("W02")=="CANDIDATE_PREPARATION_HOLD","W02 binding state invalid")
 req(all(stages.get(f"W{i:02d}")=="CANDIDATE_PREPARATION_HOLD" for i in range(3,8)),"W03-W07 candidate states invalid")
 req(all(stages.get(f"W{i:02d}")=="NOT_ASSESSED" for i in range(8,15)),"W08-W14 must remain not assessed")
 for flag in ["W01_completed","W02_completed","wireframe_allowed","visual_design_allowed","implementation_allowed"]:
  req(p.get("execution_boundary",{}).get(flag) is False,f"{flag} must remain false")
 return e
def main():
 e=validate_documents(load_all())
 if e:
  [print(f"[FAIL] {x}") for x in e]; return 1
 print("PASS_KNLSOFT_W01_W02_CANDIDATE_PREPARATION_WITH_GATES_HOLD"); return 0
if __name__=="__main__":sys.exit(main())
