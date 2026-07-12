#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location("v",R/"scripts/validate_knlsoft_w03_w07_candidates.py");v=importlib.util.module_from_spec(s);s.loader.exec_module(v);b=v.load_all()
C=[("pass_WG03",lambda d:d["w03"]["exit_gate"].__setitem__("result","PASS")),("remove_recovery",lambda d:d["w03"].__setitem__("scenarios",[x for x in d["w03"]["scenarios"] if x["class"]!="RECOVERY"])),("promote_claim",lambda d:d["w04"]["claim_contract"].__setitem__("current_verified_product_claim_count",1)),("remove_claim_gate",lambda d:d["w04"].__setitem__("publication_rules",[])),("remove_capabilities",lambda d:d["w05"].__setitem__("capabilities",[])),("remove_IA",lambda d:d["w06"].__setitem__("sitemap_candidate",[])),("remove_error_state",lambda d:d["w06"].__setitem__("global_states",[])),("remove_policy",lambda d:d["w07"].__setitem__("policies",[])),("activate_backend",lambda d:d["w07"]["execution_boundary"].__setitem__("form_backend",True)),("start_W09",lambda d:d["binding"]["stage_adoption"].__setitem__("W09","CANDIDATE_PREPARATION_HOLD"))]
for n,f in C:
 d=copy.deepcopy(b);f(d);e=v.validate_documents(d)
 if not e:raise AssertionError(n)
 print("[PASS]",n,e[0])
print(f"PASS_W03_W07_MUTATIONS_{len(C)}_OF_{len(C)}")
