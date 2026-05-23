import google.generativeai as genai
import json
import re
from config import GEMINI_API_KEY, MODEL_NAME
from prompts import SYSTEM_PROMPT, build_user_prompt

class ScenarioWriter:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not found in .env file")
        
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(
            MODEL_NAME,
            system_instruction=SYSTEM_PROMPT
        )
    
    def generate_scenario(self, input_data):
        icp_type = input_data.get("icp_type")
        milestone_code = input_data.get("milestone_code", "M01")
        skill_target = input_data.get("skill_target", "communication")
        language = input_data.get("language", "en")
        
        if not icp_type:
            raise ValueError("icp_type is required")
        if icp_type not in ["high_wage", "low_wage"]:
            raise ValueError(f"Invalid icp_type: {icp_type}")
        
        user_prompt = build_user_prompt(
            icp_type, milestone_code, skill_target, language
        )
        
        try:
            response = self.model.generate_content(user_prompt)
            raw_output = response.text
            
            json_output = self._extract_json(raw_output)
            
            self._validate_schema(json_output)
            
            return json_output
            
        except Exception as e:
            print(f"Error generating scenario: {e}")
            return self._get_fallback_scenario(icp_type, language)
    
    def _extract_json(self, text):
        text = re.sub(r'```json\s*', '', text)
        text = re.sub(r'```\s*', '', text)
        
        start = text.find('{')
        end = text.rfind('}')
        
        if start == -1 or end == -1:
            raise ValueError("No JSON object found in response")
        
        json_str = text[start:end+1]
        
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"JSON parse error: {e}")
            raise
    
    def _validate_schema(self, output):
        required_top_fields = ["scene", "characters", "antagonist_opening_line", 
                               "strategy_chips", "success_criteria", "rubric", "transfer_targets"]
        
        for field in required_top_fields:
            if field not in output:
                raise ValueError(f"Missing required field: {field}")
        
        if not all(k in output["scene"] for k in ["setting", "time", "context"]):
            raise ValueError("Scene missing setting, time, or context")
        
        if len(output["characters"]) < 2:
            raise ValueError("Need at least 2 characters")
        
        for char in output["characters"]:
            if not all(k in char for k in ["name", "role", "mood"]):
                raise ValueError("Character missing name, role, or mood")
        
        if len(output["strategy_chips"]) != 3:
            raise ValueError(f"Need exactly 3 strategy chips, got {len(output['strategy_chips'])}")
        
        for chip in output["strategy_chips"]:
            if not all(k in chip for k in ["id", "label", "philosophy"]):
                raise ValueError("Strategy chip missing id, label, or philosophy")
        
        rubric_axes = ["communication", "composure", "clarity", "strategy", "outcome"]
        for axis in rubric_axes:
            if axis not in output["rubric"]:
                raise ValueError(f"Rubric missing {axis}")
            if not isinstance(output["rubric"][axis], (int, float)):
                raise ValueError(f"Rubric {axis} must be a number")
    
    def _get_fallback_scenario(self, icp_type, language):
        is_hindi = language == "hi"
        
        if icp_type == "high_wage":
            if is_hindi:
                return {
                    "scene": {"setting": "बैंगलोर कार्यालय", "time": "सुबह 10 बजे", "context": "साप्ताहिक स्टैंडअप मीटिंग"},
                    "characters": [{"name": "रिया", "role": "सॉफ्टवेयर डेवलपर", "mood": "तनावग्रस्त"}, 
                                   {"name": "राजेश", "role": "टेक लीड", "mood": "निराश"}],
                    "antagonist_opening_line": "रिया, तुम्हारा फीचर दो दिन लेट है, पूरी टीम तुम्हारा इंतज़ार कर रही है",
                    "strategy_chips": [
                        {"id": "chip1", "label": "सफाई देना", "philosophy": "स्थिति स्पष्ट करने से ट्रस्ट बनता है"},
                        {"id": "chip2", "label": "नई डेडलाइन देना", "philosophy": "जवाबदेही दिखाता है"},
                        {"id": "chip3", "label": "मदद मांगना", "philosophy": "कमजोरी नहीं, टीमवर्क दिखाता है"}
                    ],
                    "success_criteria": ["डेडलाइन पर सहमति", "टीम का भरोसा बना रहे"],
                    "rubric": {"communication": 60, "composure": 50, "clarity": 65, "strategy": 55, "outcome": 50},
                    "transfer_targets": ["deadline management", "team communication"]
                }
            else:
                return {
                    "scene": {"setting": "Bangalore office", "time": "10 AM", "context": "Weekly standup meeting"},
                    "characters": [{"name": "Riya", "role": "Software Developer", "mood": "stressed"}, 
                                   {"name": "Rajesh", "role": "Tech Lead", "mood": "frustrated"}],
                    "antagonist_opening_line": "Riya, your feature is 2 days late, the whole team is waiting on you",
                    "strategy_chips": [
                        {"id": "chip1", "label": "Explain the blocker", "philosophy": "Transparency builds trust"},
                        {"id": "chip2", "label": "Propose new deadline", "philosophy": "Shows accountability"},
                        {"id": "chip3", "label": "Ask for help", "philosophy": "Teamwork over ego"}
                    ],
                    "success_criteria": ["Agree on new deadline", "Maintain team trust"],
                    "rubric": {"communication": 60, "composure": 50, "clarity": 65, "strategy": 55, "outcome": 50},
                    "transfer_targets": ["deadline management", "team communication"]
                }
        else:
            if is_hindi:
                return {
                    "scene": {"setting": "कस्टमर सपोर्ट सेंटर", "time": "शाम 5 बजे", "context": "ग्राहक ने एस्केलेशन किया"},
                    "characters": [{"name": "अर्जुन", "role": "डिलीवरी पार्टनर", "mood": "चिंतित"}, 
                                   {"name": "प्रिया", "role": "सुपरवाइज़र", "mood": "गंभीर"}],
                    "antagonist_opening_line": "अर्जुन, कस्टमर ने तुम्हारी शिकायत की है, बताओ क्या हुआ?",
                    "strategy_chips": [
                        {"id": "chip1", "label": "सच बताना", "philosophy": "ईमानदारी से समस्या हल होती है"},
                        {"id": "chip2", "label": "माफी मांगना", "philosophy": "गलती मानना बड़प्पन है"},
                        {"id": "chip3", "label": "समाधान देना", "philosophy": "प्रोएक्टिव बनना अच्छा है"}
                    ],
                    "success_criteria": ["शिकायत का समाधान", "सुपरवाइज़र का भरोसा"],
                    "rubric": {"communication": 55, "composure": 45, "clarity": 60, "strategy": 50, "outcome": 45},
                    "transfer_targets": ["customer handling", "problem solving"]
                }
            else:
                return {
                    "scene": {"setting": "Customer support center", "time": "5 PM", "context": "Customer escalated a complaint"},
                    "characters": [{"name": "Arjun", "role": "Delivery Partner", "mood": "anxious"}, 
                                   {"name": "Priya", "role": "Supervisor", "mood": "serious"}],
                    "antagonist_opening_line": "Arjun, a customer complained about you. Tell me what happened.",
                    "strategy_chips": [
                        {"id": "chip1", "label": "Be honest", "philosophy": "Honesty resolves conflicts"},
                        {"id": "chip2", "label": "Apologize", "philosophy": "Apology shows maturity"},
                        {"id": "chip3", "label": "Offer solution", "philosophy": "Action fixes problems"}
                    ],
                    "success_criteria": ["Resolve complaint", "Maintain supervisor trust"],
                    "rubric": {"communication": 55, "composure": 45, "clarity": 60, "strategy": 50, "outcome": 45},
                    "transfer_targets": ["customer handling", "problem solving"]
                }