#!/usr/bin/env python3
import copy
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("validator",ROOT/"scripts/validate_knlsoft_website_asset_inheritance.py")
validator=importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
source=json.loads((ROOT/"oruda/inheritance/KNLSOFT_HOMEPAGE_WEBSITE_ASSET_BINDING.v0.1.0.json").read_text(encoding="utf-8"))

cases=[
 ("local_override",lambda b:b.__setitem__("local_override",True)),
 ("embedded_copy",lambda b:b.__setitem__("embedded_common_assets",[{"id":"COPIED"}])),
 ("unpinned_commit",lambda b:b["source"].__setitem__("commit","main")),
 ("retroactive_stage_pass",lambda b:b["stage_adoption"].__setitem__("W00","PASS")),
 ("production_go",lambda b:b["execution_boundary"].__setitem__("production_go",True)),
]
for name,mutate in cases:
    binding=copy.deepcopy(source)
    mutate(binding)
    errors=validator.validate_binding(binding)
    if not errors: raise AssertionError(f"mutation escaped validation: {name}")
    print(f"[PASS] {name}: {errors[0]}")
print(f"PASS_WEBSITE_ASSET_INHERITANCE_MUTATIONS_{len(cases)}_OF_{len(cases)}")
