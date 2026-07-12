#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location("v",R/"scripts/validate_knlsoft_w08_entry.py");v=importlib.util.module_from_spec(s);s.loader.exec_module(v);b=v.load_all()
C=[("remove_OManager",lambda d:d["a"].__setitem__("instances",[x for x in d["a"]["instances"] if x["role"]!="OManager"])),("activate_PM",lambda d:d["a"].__setitem__("inactive_roles",["OProjectLeader","OBuilder"])),("production_go",lambda d:d["a"].__setitem__("production_go",True)),("open_WG08",lambda d:d["r"]["entry_gate"].__setitem__("result","PASS")),("allow_wireframe",lambda d:d["r"].__setitem__("wireframe_allowed",True)),("create_wireframe",lambda d:d["r"].__setitem__("wireframe_candidate",{})),("define_layout",lambda d:d["p"].__setitem__("layout_defined",True)),("define_interaction_wireframe",lambda d:d["i"].__setitem__("wireframe_defined",True)),("remove_sources",lambda d:d["s"].__setitem__("items",[])),("start_W09",lambda d:d["b"]["stage_adoption"].__setitem__("W09","CANDIDATE_PREPARATION_HOLD"))]
for n,f in C:
 d=copy.deepcopy(b);f(d);e=v.validate_documents(d)
 if not e:raise AssertionError(n)
 print("[PASS]",n,e[0])
print(f"PASS_W08_MUTATIONS_{len(C)}_OF_{len(C)}")
