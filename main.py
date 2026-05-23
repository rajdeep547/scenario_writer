import json
import sys
import os
from scenario_writer import ScenarioWriter

def main():
    print("Scenario Writer - AI Module")
    print("=" * 40)
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        
        if not os.path.exists(input_file):
            print(f"❌ Error: File '{input_file}' not found!")
            print("\nCreating a sample input.json for you...")
            
            sample_input = {
                "icp_type": "high_wage",
                "milestone_code": "M01",
                "skill_target": "technical_communication",
                "language": "en"
            }
            
            with open("input.json", "w", encoding='utf-8') as f:
                json.dump(sample_input, f, indent=2)
            
            print("✅ Created sample input.json")
            print("Run again: python main.py input.json\n")
            return
        
        with open(input_file, 'r', encoding='utf-8') as f:
            input_data = json.load(f)
    else:
        print("\n📝 Interactive Mode - Enter scenario details:")
        print("-" * 40)
        
        icp_type = input("ICP Type (high_wage/low_wage): ").strip()
        milestone_code = input("Milestone Code (M01-M07): ").strip()
        skill_target = input("Skill Target: ").strip()
        language = input("Language (en/hi): ").strip()
        
        input_data = {
            "icp_type": icp_type,
            "milestone_code": milestone_code,
            "skill_target": skill_target,
            "language": language
        }
        
        save = input("\nSave this input to file? (y/n): ").strip().lower()
        if save == 'y':
            filename = input("Filename (e.g., my_scenario.json): ").strip()
            if not filename.endswith('.json'):
                filename += '.json'
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(input_data, f, indent=2)
            print(f"✅ Saved to {filename}")
    
    print("\n" + "=" * 40)
    print("🎬 Generating scenario...")
    print("=" * 40)
    
    try:
        writer = ScenarioWriter()
        output = writer.generate_scenario(input_data)
        
        print("\n✅ Generated Scenario:")
        print(json.dumps(output, indent=2, ensure_ascii=False))
        
        output_file = "output_scenario.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        
        print(f"\n📁 Output saved to: {output_file}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Troubleshooting:")
        print("1. Check if GEMINI_API_KEY is set in .env file")
        print("2. Verify your internet connection")
        print("3. Make sure you have installed: pip install google-generativeai python-dotenv")

if __name__ == "__main__":
    main()