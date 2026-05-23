import os
import json
import glob
import sys

def check_files():
    print("=" * 60)
    print("FINAL SUBMISSION CHECK")
    print("=" * 60)
    
    required_files = [
        "config.py", "prompts.py", "scenario_writer.py", 
        "test_cases.py", "run_tests.py", "main.py",
        "requirements.txt", "README.md"
    ]
    
    print("\n📁 Required Files:")
    all_exist = True
    for f in required_files:
        if os.path.exists(f):
            print(f"  ✅ {f}")
        else:
            print(f"  ❌ {f} - MISSING")
            all_exist = False
    
    return all_exist

def check_tests():
    print("\n🧪 Test Results:")
    test_files = glob.glob("test_results_*.json")
    if test_files:
        latest = max(test_files)
        print(f"  ✅ Found: {latest}")
        
        with open(latest, 'r', encoding='utf-8') as f:
            results = json.load(f)
        
        passed = sum(1 for r in results if r.get("status") == "PASSED")
        print(f"  📊 Tests passed: {passed}/10")
        
        if passed == 10:
            print("  🎉 All 10 tests passed!")
            return True
        else:
            print(f"  ⚠️ Only {passed}/10 passed. Run python run_tests.py")
            return False
    else:
        print("  ❌ No test results found. Run python run_tests.py first")
        return False

def check_schema():
    print("\n📋 Schema Validation:")
    test_files = glob.glob("test_results_*.json")
    if not test_files:
        return False
    
    with open(max(test_files), 'r', encoding='utf-8') as f:
        results = json.load(f)
    
    valid_count = 0
    for r in results:
        if r.get("status") == "PASSED" and "output" in r:
            output = r["output"]
            
            # Check required fields
            has_fields = all(f in output for f in ["scene", "characters", "antagonist_opening_line", 
                                                     "strategy_chips", "success_criteria", "rubric", "transfer_targets"])
            
            # Check strategy chips
            chips_ok = len(output.get("strategy_chips", [])) == 3
            
            # Check rubric not all 50s
            rubric = output.get("rubric", {})
            not_all_50 = not all(v == 50 for v in rubric.values())
            
            if has_fields and chips_ok and not_all_50:
                valid_count += 1
    
    print(f"  ✅ Schema valid: {valid_count}/10")
    return valid_count == 10

def main():
    print("\n🔍 RUNNING FINAL VERIFICATION...\n")
    
    files_ok = check_files()
    tests_ok = check_tests()
    schema_ok = check_schema()
    
    print("\n" + "=" * 60)
    print("FINAL SCORE")
    print("=" * 60)
    
    score = 0
    if files_ok:
        print("✅ Files present: +10 pts")
        score += 10
    else:
        print("❌ Missing files: 0 pts")
    
    if tests_ok:
        print("✅ All tests pass: +15 pts")
        score += 15
    else:
        print("❌ Tests failing: 0 pts")
    
    if schema_ok:
        print("✅ Schema valid: +25 pts")
        score += 25
    else:
        print("❌ Schema invalid: 0 pts")
    
    print(f"\n📊 TOTAL SCORE: {score}/50 (before demo call)")
    
    if score >= 40:
        print("\n🎉 READY FOR SUBMISSION! Great work!")
        print("\nNext steps:")
        print("1. Run: python final_check.py again")
        print("2. Create PROMPT_DEFENSE.md")
        print("3. Record 5-min demo video")
        print("4. Push to GitHub: git push")
    else:
        print("\n⚠️ Need improvements before submission")
        print("Run: python run_tests.py to fix failing tests")
    
    return score

if __name__ == "__main__":
    main()