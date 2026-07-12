#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/"oruda/inheritance/KNLSOFT_HOMEPAGE_WEBSITE_ASSET_BINDING.v0.1.0.json"

def validate_binding(binding):
    errors=[]
    def require(condition,message):
        if not condition: errors.append(message)
    require(binding.get("binding_id")=="KNLSOFT-HOMEPAGE-WEBSITE-PROGRAM-ASSET-BINDING","invalid binding id")
    source=binding.get("source",{})
    require(source.get("repository")=="babyandi/ORUDA","ORUDA must own common assets")
    require(source.get("asset_domain_id")=="ORUDA-WEBSITE-PROGRAM-ASSET-DOMAIN","invalid upstream domain")
    require(source.get("commit")=="102b84c091e132cf965c4f47e3c0daa5d617bb2a","upstream commit must be pinned")
    require(binding.get("inheritance_mode")=="PINNED_REFERENCE","inheritance must be pinned reference")
    require(binding.get("local_override") is False,"local override must be false")
    require(binding.get("embedded_common_assets")==[],"common assets must not be embedded")
    expected=[f"W{i:02d}" for i in range(15)]
    stages=binding.get("stage_adoption",{})
    require(list(stages.keys())==expected,"W00-W14 adoption ledger required")
    require(stages.get("W00")=="PREPARATION_IN_PROGRESS_HOLD","W00 must remain preparation HOLD")
    require(stages.get("W01")=="CANDIDATE_PREPARATION_HOLD","W01 candidate state invalid")
    require(stages.get("W02")=="CANDIDATE_PREPARATION_HOLD","W02 candidate state invalid")
    require(all(stages.get(f"W{i:02d}")=="NOT_ASSESSED" for i in range(3,15)),"W03-W14 must remain not assessed")
    require(binding.get("prior_documents")=="ORUDA_INTAKE_INPUT_CANDIDATE","prior documents cannot be treated as stage PASS")
    boundary=binding.get("execution_boundary",{})
    for flag in ["website_rebuilt","runtime_execution","actual_test_execution","production_go","commercial_go","final_lock"]:
        require(boundary.get(flag) is False,f"{flag} must remain false")
    return errors

def main():
    binding=json.loads(PATH.read_text(encoding="utf-8"))
    errors=validate_binding(binding)
    if errors:
        for error in errors: print(f"[FAIL] {error}")
        return 1
    print("PASS_KNLSOFT_WEBSITE_ASSET_INHERITANCE")
    return 0

if __name__=="__main__":
    sys.exit(main())
