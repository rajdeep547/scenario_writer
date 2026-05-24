from scenario_writer import ScenarioWriter
import json

writer = ScenarioWriter()

# Test different skills
test_cases = [
    {"icp_type": "high_wage", "skill_target": "negotiation", "language": "en"},
    {"icp_type": "high_wage", "skill_target": "public_speaking", "language": "en"},
    {"icp_type": "high_wage", "skill_target": "time_management", "language": "en"},
    {"icp_type": "low_wage", "skill_target": "customer_service", "language": "en"},
    {"icp_type": "high_wage", "skill_target": "technical_writing", "language": "en"},
]

print("=" * 70)
print("TESTING DIFFERENT SKILL TARGETS")
print("=" * 70)

for i, test in enumerate(test_cases, 1):
    print(f"\n{'='*70}")
    print(f"TEST {i}: Skill = '{test['skill_target']}'")
    print(f"{'='*70}")
    
    result = writer.generate_scenario(test)
    
    print(f"\n📌 Setting: {result['scene']['setting']}")
    print(f"🎭 Antagonist: {result['antagonist_opening_line']}")
    print(f"💡 First Strategy: {result['strategy_chips'][0]['label']}")
    print(f"✅ Success Criteria: {result['success_criteria'][0]}")
    print(f"🏆 Transfer Targets: {result['transfer_targets'][0]}")
    print("\n" + "-" * 70)
    