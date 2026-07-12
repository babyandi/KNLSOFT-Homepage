#!/usr/bin/env python3
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
P={f"w0{i}":f"oruda/website/W0{i}/KNLSOFT_WEBSITE_W0{i}_{n}.v0.1.0.json" for i,n in [(3,"JOB_JOURNEY_SCENARIO"),(4,"CONTENT_DATA_EVIDENCE"),(5,"FUNCTIONAL_ARCHITECTURE"),(6,"IA_NAV_TASK_STATE"),(7,"POLICY_PERMISSION_SECURITY")]}
P["binding"]="oruda/inheritance/KNLSOFT_HOMEPAGE_WEBSITE_ASSET_BINDING.v0.1.0.json"
def load_all():return {k:json.loads((R/v).read_text()) for k,v in P.items()}
def validate_documents(d):
 e=[];q=lambda c,m:e.append(m) if not c else None
 for i in range(3,8):
  x=d[f"w0{i}"];q(x.get("status")=="CANDIDATE_PREPARATION_HOLD",f"W0{i} status invalid");q(x.get("entry_dependency",{}).get("formal_execution") is False,f"W0{i} formal execution opened");q(x.get("exit_gate",{}).get("result")=="HOLD",f"WG-0{i} must remain HOLD")
 q({x.get("class") for x in d["w03"].get("scenarios",[])}=={"NORMAL","EXCEPTION","RECOVERY"},"W03 scenario coverage incomplete")
 q(d["w04"].get("claim_contract",{}).get("current_verified_product_claim_count")==0,"unverified claims promoted")
 q("NO_EVIDENCE_NO_FACT" in d["w04"].get("publication_rules",[]),"claim gate missing")
 q(len(d["w05"].get("capabilities",[]))>=10,"functional coverage incomplete")
 q(len(d["w06"].get("sitemap_candidate",[]))>=9,"IA coverage incomplete")
 q("VALIDATION_ERROR" in d["w06"].get("global_states",[]),"error state missing")
 q(len(d["w07"].get("policies",[]))>=8,"policy coverage incomplete")
 q(d["w07"].get("execution_boundary",{}).get("form_backend") is False,"backend falsely activated")
 s=d["binding"].get("stage_adoption",{})
 for i in range(1,8):q(s.get(f"W{i:02d}")=="CANDIDATE_PREPARATION_HOLD",f"W{i:02d} candidate state invalid")
 q(s.get("W08")=="ENTRY_PREPARATION_HOLD","W08 entry state invalid")
 for i in range(9,15):q(s.get(f"W{i:02d}")=="NOT_ASSESSED",f"W{i:02d} must remain not assessed")
 return e
def main():
 e=validate_documents(load_all())
 if e:[print("[FAIL]",x) for x in e];return 1
 print("PASS_KNLSOFT_W03_W07_CANDIDATE_PREPARATION");return 0
if __name__=="__main__":sys.exit(main())
