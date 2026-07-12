#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("v",ROOT/"scripts/validate_knlsoft_role_inheritance.py")
if spec is None or spec.loader is None:raise RuntimeError("VALIDATOR_LOAD_FAILED")
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v);base=v.load(v.BINDING_PATH)
def case(mutate,expected):
    b=copy.deepcopy(base);mutate(b);return expected in v.validate_document(b)
def main():
    cases={
      "local_override":case(lambda x:x.update(local_override=True),"INHERITANCE_FAIL_OPEN"),
      "embedded_copy":case(lambda x:x["embedded_role_definitions"].append({"role_id":"LOCAL"}),"LOCAL_ROLE_COPY_FORBIDDEN"),
      "source_unpinned":case(lambda x:x.update(source_commit_sha="main"),"SOURCE_PIN_INVALID"),
      "role_activated":case(lambda x:x["project_instance_boundary"].update(actual_role_instances_created=True),"ROLE_ACTIVATION_BOUNDARY_FAIL_OPEN")
    }
    failed=[k for k,vv in cases.items() if not vv]
    print(json.dumps({"harness":"test_knlsoft_role_inheritance_mutations.py","decision":"PASS" if not failed else "BLOCK","cases":len(cases),"failed":failed,"runtime_execution":False},ensure_ascii=False,indent=2))
    return 0 if not failed else 1
if __name__=="__main__":raise SystemExit(main())
