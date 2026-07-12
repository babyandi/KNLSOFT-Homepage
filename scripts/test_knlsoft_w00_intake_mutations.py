#!/usr/bin/env python3
import copy
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("v",ROOT/"scripts/validate_knlsoft_w00_intake.py")
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
base=v.load_all()
cases=[
 ("premature_W00_pass",lambda d:d["intake"]["gate"].__setitem__("exit_result","PASS")),
 ("allow_downstream",lambda d:d["intake"]["gate"].__setitem__("downstream_stage_completion_allowed",True)),
 ("remove_product_source_gap",lambda d:d["sources"].__setitem__("missing_official_sources",[])),
 ("approve_decision_without_evidence",lambda d:d["decisions"]["items"][0].__setitem__("state","APPROVED")),
 ("remove_recovery",lambda d:d["scenarios"].__setitem__("scenarios",[x for x in d["scenarios"]["scenarios"] if x["class"]!="RECOVERY"])),
 ("omit_OManager",lambda d:d["roles"].__setitem__("delegation_spine",[x for x in d["roles"]["delegation_spine"] if x!="OManager"])),
 ("activate_PM",lambda d:next(x for x in d["roles"]["W00_authority"] if x["role"]=="OProjectManager").__setitem__("activation","ACTIVE")),
 ("create_role_instance",lambda d:d["roles"].__setitem__("actual_role_instances",[{"role":"OBuilder"}])),
 ("mark_W01_complete",lambda d:d["intake"]["execution_boundary"].__setitem__("W01_completed",True)),
 ("start_visual_design",lambda d:d["intake"]["execution_boundary"].__setitem__("visual_design_allowed",True)),
]
for name,mutate in cases:
    d=copy.deepcopy(base); mutate(d); errors=v.validate_documents(d)
    if not errors: raise AssertionError(f"mutation escaped validation: {name}")
    print(f"[PASS] {name}: {errors[0]}")
print(f"PASS_W00_MUTATION_HARNESS_{len(cases)}_OF_{len(cases)}")
