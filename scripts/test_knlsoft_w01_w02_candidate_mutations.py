#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("v",ROOT/"scripts/validate_knlsoft_w01_w02_candidates.py")
v=importlib.util.module_from_spec(s);s.loader.exec_module(v);base=v.load_all()
cases=[
 ("pass_WG01",lambda d:d["purpose"]["exit_gate"].__setitem__("result","PASS")),
 ("formal_W01",lambda d:d["purpose"]["entry_dependency"].__setitem__("formal_W01_execution_allowed",True)),
 ("approve_outcome",lambda d:d["purpose"]["business_outcome_candidates"][0].__setitem__("status","APPROVED")),
 ("invent_numeric_target",lambda d:d["measures"]["measures"][0].__setitem__("target","50%")),
 ("pass_WG02",lambda d:d["users"]["exit_gate"].__setitem__("result","PASS")),
 ("verify_user_without_research",lambda d:d["users"]["user_groups"][0].__setitem__("evidence_status","VERIFIED")),
 ("remove_buyer_role",lambda d:d["buying"]["decision_roles"].pop()),
 ("remove_recovery",lambda d:d["buying"].__setitem__("exceptions",[])),
 ("start_W03",lambda d:d["binding"]["stage_adoption"].__setitem__("W03","CANDIDATE_PREPARATION_HOLD")),
 ("allow_wireframe",lambda d:d["purpose"]["execution_boundary"].__setitem__("wireframe_allowed",True))]
for n,f in cases:
 d=copy.deepcopy(base);f(d);e=v.validate_documents(d)
 if not e:raise AssertionError(f"mutation escaped validation: {n}")
 print(f"[PASS] {n}: {e[0]}")
print(f"PASS_W01_W02_MUTATION_HARNESS_{len(cases)}_OF_{len(cases)}")
