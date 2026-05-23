import json
import glob

def validate_schema(output):
    """Check if output matches required schema"""
    required_fields = ["scene", "characters", "antagonist_opening_line", 
                       "strategy_chips", "success_criteria", "rubric", "transfer_targets"]
    
    for field in required_fields:
        if field not in output:
            return False, f"Missing {field}"
    
    if "setting" not in output["scene"] or "time" not in output["scene"] or "context" not in output["scene"]:
        return False, "Scene missing setting, time, or context"
    
    if len(output["characters"]) < 2:
        return False, "Need at least 2 characters"
    
    if len(output["strategy_chips"]) != 3:
        return False, f"Need exactly 3 strategy chips, got {len(output['strategy_chips'])}"
    
    philosophies = [chip.get("philosophy", "") for chip in output["strategy_chips"]]
    if len(set(philosophies)) < 2:
        return False, "Strategy chips are too similar"
    
    rubric_values = list(output["rubric"].values())
    if all(v == 50 for v in rubric_values):
        return False, "All rubric scores are 50 - auto fail"
    
    return True, "Valid"

# Find the most recent test results file
test_files = glob.glob("test_results_*.json")
if not test_files:
    print("❌ No test results found. Run python run_tests.py first")
    exit()

latest_file = max(test_files)  # Get the most recent
print(f"📂 Loading: {latest_file}")

with open(latest_file, "r", encoding="utf-8") as f:
    results = json.load(f)

print("=" * 60)
print("SCHEMA VALIDATION RESULTS")
print("=" * 60)

passed = 0
for result in results:
    test_id = result.get("test_id", "?")
    status = result.get("status", "UNKNOWN")
    
    if status == "PASSED" and "output" in result:
        valid, msg = validate_schema(result["output"])
        if valid:
            passed += 1
            print(f"✅ Test {test_id}: {msg}")
        else:
            print(f"❌ Test {test_id}: {msg}")
    else:
        print(f"❌ Test {test_id}: {result.get('error', 'Test failed')}")

print("=" * 60)
print(f"RESULTS: {passed}/10 tests passed schema validation")
print("=" * 60)

if passed == 10:
    print("🎉 PERFECT! 30/30 points for schema correctness")
else:
    print(f"⚠️ Need {10-passed} more to pass. Fix failing tests.")