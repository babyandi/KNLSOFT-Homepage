import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
contract = json.loads((ROOT / "KNLSOFT_ARTIFACT_REMEDIATION_CONTRACT.v1.0.0.json").read_text())
expected = {f"KNL-AF-{number:03d}" for number in range(1, 14)}

assert contract["state"] == "DESIGN_VALIDATED_REWORK_NOT_EXECUTED"
assert contract["baseline"]["program_registry"].endswith("P01_P27")
covered = {item for group in contract["finding_groups"] for item in group["finding_ids"]}
assert covered == expected
assert len(covered) == 13
for group in contract["finding_groups"]:
    assert group["required_rework"]
    assert group["acceptance_oracle"]
    assert group["evidence"]
    assert group["failure_path"]
roles = contract["assurance_chain"]
assert roles["artifact_author"] != roles["independent_review_owner"]
assert roles["artifact_author"] != roles["decision_authority"]
assert contract["protected_boundaries"]["implementation"] == "HOLD"
print("PASS: remediation contract structure and 13-finding coverage")
