#!/usr/bin/env python3
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
P={"a":"oruda/project/KNLSOFT_WEBSITE_AUTHORITY_BINDING.v0.1.0.json","r":"oruda/website/W08/KNLSOFT_WEBSITE_W08_ENTRY_READINESS.v0.1.0.json","p":"oruda/website/W08/KNLSOFT_WEBSITE_W08_PAGE_RESPONSIBILITY.v0.1.0.json","i":"oruda/website/W08/KNLSOFT_WEBSITE_W08_INTERACTION_CONTRACT.v0.1.0.json","s":"oruda/website/W08/KNLSOFT_WEBSITE_W08_OFFICIAL_SOURCE_REQUEST.v0.1.0.json","b":"oruda/inheritance/KNLSOFT_HOMEPAGE_WEBSITE_ASSET_BINDING.v0.1.0.json"}
def load_all():return {k:json.loads((R/v).read_text()) for k,v in P.items()}
def validate_documents(d):
 e=[];q=lambda c,m:e.append(m) if not c else None
 a,r,p,i,s,b=[d[x] for x in "arpisb"]
 roles={x.get("role"):x for x in a.get("instances",[])}
 q(set(roles)=={"HUMAN_DECISION_OWNER","OManager"},"authority instances invalid")
 q(roles.get("OManager",{}).get("state")=="ACTIVE_FOR_GO_HOLD_CONTROL","OManager not bound")
 q(a.get("inactive_roles")==["OProjectManager","OProjectLeader","OBuilder"],"delivery roles activated")
 for x in ["production_go","commercial_go","final_lock"]:q(a.get(x) is False,f"{x} must remain false")
 q(r.get("status")=="ENTRY_PREPARATION_HOLD","W08 status invalid");q(r.get("entry_gate",{}).get("result")=="HOLD","WG08 opened");q(r.get("wireframe_allowed") is False and r.get("wireframe_candidate") is None,"wireframe created");q(r.get("visual_design_allowed") is False,"visual design opened")
 q(len(p.get("pages",[]))==9 and p.get("layout_defined") is False,"page responsibility/layout boundary invalid")
 q(i.get("wireframe_defined") is False and len(i.get("patterns",[]))>=5,"interaction contract invalid")
 q(len(s.get("items",[]))>=6,"official source request incomplete")
 st=b.get("stage_adoption",{});q(st.get("W08")=="ENTRY_PREPARATION_HOLD","binding W08 invalid");q(all(st.get(f"W{x:02d}")=="NOT_ASSESSED" for x in range(9,15)),"W09-W14 must remain not assessed")
 return e
def main():
 e=validate_documents(load_all())
 if e:[print("[FAIL]",x) for x in e];return 1
 print("PASS_KNLSOFT_W08_ENTRY_PREPARATION_HOLD");return 0
if __name__=="__main__":sys.exit(main())
