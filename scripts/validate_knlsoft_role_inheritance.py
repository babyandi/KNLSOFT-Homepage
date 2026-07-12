#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[1]
BINDING_PATH=ROOT/"oruda/inheritance/KNLSOFT_HOMEPAGE_OBUILDER_ROLE_BINDING.v1.0.0.json"
EXPECTED_COMMIT="f72b0290c81a6bbe52cd4aed6ee2c438f1ecad86"
REQUIRED_SELECTED={"OBR-PLAN-IMPL","OBR-ARC-SW","OBR-DES-UIUX","OBR-DEV-FE","OBR-DEV-BE","OBR-DATA-DA","OBR-DATA-DBA","OBR-QA-A11Y"}
REQUIRED_DEFERRED_HW={"OBR-ARC-HW","OBR-PLAT-HW"}
def load(path:Path)->dict[str,Any]:return json.loads(path.read_text(encoding="utf-8"))
def validate_document(b:dict[str,Any])->list[str]:
    e=[]
    if b.get("taxonomy_id")!="ORUDA_OBUILDER_ROLE_TAXONOMY_V1_0_0" or b.get("taxonomy_version")!="1.0.0":e.append("TAXONOMY_REFERENCE_INVALID")
    if b.get("source_repository")!="babyandi/ORUDA" or b.get("source_commit_sha")!=EXPECTED_COMMIT:e.append("SOURCE_PIN_INVALID")
    if b.get("inheritance_mode")!="PINNED_REFERENCE" or b.get("local_override") is not False:e.append("INHERITANCE_FAIL_OPEN")
    if b.get("embedded_role_definitions")!=[]:e.append("LOCAL_ROLE_COPY_FORBIDDEN")
    if b.get("delegation_spine_ref")!="ORUDA_OBUILDER_ROLE_TAXONOMY_V1_0_0.delegation_spine":e.append("DELEGATION_REFERENCE_INVALID")
    selected=set(b.get("activation_profile",{}).get("selected_role_ids",[]))
    if not REQUIRED_SELECTED.issubset(selected):e.append("REQUIRED_PROJECT_ROLE_SELECTION_MISSING")
    deferred=set(b.get("activation_profile",{}).get("deferred_until_physical_infra_scope",[]))
    if not REQUIRED_DEFERRED_HW.issubset(deferred):e.append("HARDWARE_ROLE_INHERITANCE_MISSING")
    boundary=b.get("project_instance_boundary",{})
    if not boundary or any(v is not False for v in boundary.values()):e.append("ROLE_ACTIVATION_BOUNDARY_FAIL_OPEN")
    if b.get("extension_route")!="ORUDA_ROLE_GOVERNANCE_CHANGE_REQUEST":e.append("EXTENSION_ROUTE_INVALID")
    return e
def main()->int:
    try:e=["BINDING_MISSING"] if not BINDING_PATH.is_file() else validate_document(load(BINDING_PATH))
    except Exception as ex:e=[f"VALIDATION_EXCEPTION:{type(ex).__name__}:{ex}"]
    print(json.dumps({"validator":"validate_knlsoft_role_inheritance.py","decision":"PASS_PINNED_REFERENCE_CANDIDATE" if not e else "BLOCK","role_instances_created":False,"runtime_execution":False,"production_go":False,"errors":e},ensure_ascii=False,indent=2))
    return 0 if not e else 1
if __name__=="__main__":raise SystemExit(main())
