import os
from dotenv import load_dotenv

load_dotenv()

# OPTION 1: Try to get from .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# OPTION 2: If not found, use this hardcoded key (REMOVE AFTER TESTING)
# Replace "YOUR_REAL_API_KEY_HERE" with your actual key
if not GEMINI_API_KEY:
    GEMINI_API_KEY = "AIzaSyDqqNYWGU0AhuLTEGtLOASX51yBLCvOYLI"  # <--- PUT YOUR KEY HERE

MODEL_NAME = "gemini-1.5-pro"

ICP_HIGH_WAGE = "high_wage"
ICP_LOW_WAGE = "low_wage"

MILESTONES = ["M01", "M02", "M03", "M04", "M05", "M06", "M07"]

REQUIRED_SCHEMA_FIELDS = [
    "scene", 
    "characters", 
    "antagonist_opening_line", 
    "strategy_chips", 
    "success_criteria", 
    "rubric", 
    "transfer_targets"
]

RUBRIC_AXES = [
    "communication", 
    "composure", 
    "clarity", 
    "strategy", 
    "outcome"
]

LANGUAGE_ENGLISH = "en"
LANGUAGE_HINDI = "hi"

DEFAULT_EPISODE_TITLE = "Workplace Challenge"
DEFAULT_MILESTONE = "M01"
DEFAULT_SKILL_TARGET = "communication"
DEFAULT_LANGUAGE = "en"

def validate_config():
    if not GEMINI_API_KEY:
        raise ValueError(
            "❌ GEMINI_API_KEY not found!\n"
            "Please create a .env file with:\n"
            "GEMINI_API_KEY=your_api_key_here\n\n"
            "Get your API key from: https://makersuite.google.com/app/apikey"
        )
    return True

if __name__ == "__main__":
    print("Configuration loaded:")
    print(f"  - API Key present: {'✅ Yes' if GEMINI_API_KEY else '❌ No'}")
    print(f"  - Model: {MODEL_NAME}")
    print(f"  - ICP Types: {ICP_HIGH_WAGE}, {ICP_LOW_WAGE}")
    print(f"  - Milestones: {MILESTONES}")
    print(f"  - Rubric axes: {RUBRIC_AXES}")