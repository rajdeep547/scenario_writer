import json
from datetime import datetime
from scenario_writer import ScenarioWriter
from test_cases import test_inputs

def run_all_tests():
    print("=" * 60)
    print("SCENARIO WRITER - TEST RUN")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    writer = ScenarioWriter()
    results = []
    
    for i, test_input in enumerate(test_inputs, 1):
        print(f"\n[Test {i}/{len(test_inputs)}]")
        print(f"ICP: {test_input['icp_type']}, Language: {test_input['language']}")
        print(f"Milestone: {test_input['milestone_code']}, Skill: {test_input['skill_target']}")
        print("-" * 40)
        
        try:
            output = writer.generate_scenario(test_input)
            
            result = {
                "test_id": i,
                "input": test_input,
                "output": output,
                "status": "PASSED"
            }
            results.append(result)
            
            print(f"✅ PASSED")
            print(f"   Scene: {output['scene']['setting']}")
            print(f"   Antagonist: {output['antagonist_opening_line'][:60]}...")
            print(f"   Rubric scores: {output['rubric']}")
            
        except Exception as e:
            print(f"❌ FAILED: {e}")
            results.append({
                "test_id": i,
                "input": test_input,
                "error": str(e),
                "status": "FAILED"
            })
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for r in results if r["status"] == "PASSED")
    failed = len(results) - passed
    
    print(f"Total: {len(results)}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"test_results_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\nResults saved to: test_results_{timestamp}.json")
    
    return results

if __name__ == "__main__":
    run_all_tests()