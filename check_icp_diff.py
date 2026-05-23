import json
import glob

# Find the most recent test results file
test_files = glob.glob("test_results_*.json")
if not test_files:
    print("❌ No test results found. Run python run_tests.py first")
    exit()

latest_file = max(test_files)
print(f"📂 Loading: {latest_file}\n")

with open(latest_file, "r", encoding="utf-8") as f:
    results = json.load(f)

high_wage_outputs = []
low_wage_outputs = []
high_wage_inputs = []
low_wage_inputs = []

for r in results:
    if r.get("status") == "PASSED" and "output" in r:
        icp = r.get("input", {}).get("icp_type", "")
        if icp == "high_wage":
            high_wage_outputs.append(r["output"])
            high_wage_inputs.append(r["input"])
        elif icp == "low_wage":
            low_wage_outputs.append(r["output"])
            low_wage_inputs.append(r["input"])

print("=" * 60)
print("ICP DIFFERENTIATION CHECK")
print("=" * 60)

# Check high_wage outputs
print("\n📊 HIGH_WAGE Samples (5 scenarios):")
for i, out in enumerate(high_wage_outputs[:3]):
    inp = high_wage_inputs[i] if i < len(high_wage_inputs) else {}
    print(f"\n  {i+1}. Episode: {inp.get('episode_title', 'N/A')}")
    print(f"     Setting: {out['scene']['setting']}")
    print(f"     Antagonist: {out['antagonist_opening_line'][:70]}...")
    print(f"     Characters: {[c['role'] for c in out['characters']]}")

# Check low_wage outputs
print("\n📊 LOW_WAGE Samples (5 scenarios):")
for i, out in enumerate(low_wage_outputs[:3]):
    inp = low_wage_inputs[i] if i < len(low_wage_inputs) else {}
    print(f"\n  {i+1}. Episode: {inp.get('episode_title', 'N/A')}")
    print(f"     Setting: {out['scene']['setting']}")
    print(f"     Antagonist: {out['antagonist_opening_line'][:70]}...")
    print(f"     Characters: {[c['role'] for c in out['characters']]}")

# Verification
print("\n" + "=" * 60)
print("VERIFICATION RESULTS")
print("=" * 60)

high_settings = ' '.join([out['scene']['setting'].lower() for out in high_wage_outputs])
low_settings = ' '.join([out['scene']['setting'].lower() for out in low_wage_outputs])

tech_keywords = ['tech', 'software', 'office', 'bangalore', 'standup', 'code']
service_keywords = ['customer', 'support', 'delivery', 'center', 'service']

if any(kw in high_settings for kw in tech_keywords):
    print("✅ High_wage has tech/office settings")
    points = 12
else:
    print("⚠️ High_wage missing tech context")
    points = 0

if any(kw in low_settings for kw in service_keywords):
    print("✅ Low_wage has customer/service settings")
    points += 13
else:
    print("⚠️ Low_wage missing service context")

print(f"\n📊 ICP Differentiation Score: {points}/25 points")

if points >= 20:
    print("🎉 Excellent! Strong differentiation between user types")
elif points >= 15:
    print("✅ Good differentiation, minor improvements possible")
else:
    print("⚠️ Need more differentiation between ICP types")