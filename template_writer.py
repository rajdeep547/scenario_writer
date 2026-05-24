import json
from typing import Dict, Any

class TemplateScenarioWriter:
    """Returns pre-defined scenarios based on input - 100% consistent"""
    
    def __init__(self):
        self.templates = self.load_templates()
    
    def load_templates(self):
        """Load pre-defined scenario templates"""
        return {
            # High Wage Templates
            "high_wage_M01_communication_en": {
                "scene": {
                    "setting": "Bangalore tech office, meeting room",
                    "time": "10:30 AM, during daily standup",
                    "context": "You missed a deadline for the authentication module"
                },
                "characters": [
                    {"name": "Priya", "role": "Tech Lead", "mood": "frustrated"},
                    {"name": "Rahul", "role": "Software Engineer", "mood": "defensive"}
                ],
                "antagonist_opening_line": "Rahul, you said the auth module would be done yesterday. The client demo is in 4 hours. What happened?",
                "strategy_chips": [
                    {"id": "chip1", "label": "Explain the blocker", "philosophy": "Transparency builds trust"},
                    {"id": "chip2", "label": "Propose new timeline", "philosophy": "Shows accountability"},
                    {"id": "chip3", "label": "Ask for help", "philosophy": "Teamwork over ego"}
                ],
                "success_criteria": ["Agree on new deadline", "Maintain team trust"],
                "rubric": {"communication": 65, "composure": 50, "clarity": 70, "strategy": 55, "outcome": 50},
                "transfer_targets": ["deadline management", "team communication"]
            },
            
            "high_wage_M01_communication_hi": {
                "scene": {
                    "setting": "बैंगलोर कार्यालय",
                    "time": "सुबह 10:30 बजे",
                    "context": "आपने ऑथेंटिकेशन मॉड्यूल की डेडलाइन मिस कर दी"
                },
                "characters": [
                    {"name": "प्रिया", "role": "टेक लीड", "mood": "निराश"},
                    {"name": "राहुल", "role": "सॉफ्टवेयर इंजीनियर", "mood": "बचाव में"}
                ],
                "antagonist_opening_line": "राहुल, तुमने कल कहा था कि ऑथ मॉड्यूल हो जाएगा। क्लाइंट डेमो 4 घंटे में है। क्या हुआ?",
                "strategy_chips": [
                    {"id": "chip1", "label": "समस्या बताएं", "philosophy": "पारदर्शिता से विश्वास बनता है"},
                    {"id": "chip2", "label": "नई समयसीमा दें", "philosophy": "जवाबदेही दिखाता है"},
                    {"id": "chip3", "label": "मदद मांगे", "philosophy": "टीमवर्क अहम है"}
                ],
                "success_criteria": ["नई डेडलाइन पर सहमति", "टीम का विश्वास बनाए रखें"],
                "rubric": {"communication": 65, "composure": 50, "clarity": 70, "strategy": 55, "outcome": 50},
                "transfer_targets": ["डेडलाइन प्रबंधन", "टीम संचार"]
            },
            
            # Low Wage Templates
            "low_wage_M01_customer_handling_hi": {
                "scene": {
                    "setting": "कस्टमर सपोर्ट सेंटर",
                    "time": "शाम 5 बजे",
                    "context": "एक ग्राहक ने शिकायत की है"
                },
                "characters": [
                    {"name": "अर्जुन", "role": "डिलीवरी पार्टनर", "mood": "चिंतित"},
                    {"name": "प्रिया", "role": "सुपरवाइज़र", "mood": "गंभीर"}
                ],
                "antagonist_opening_line": "अर्जुन, एक ग्राहक ने तुम्हारी शिकायत की है। बताओ क्या हुआ?",
                "strategy_chips": [
                    {"id": "chip1", "label": "सच बताएं", "philosophy": "ईमानदारी से समस्या हल होती है"},
                    {"id": "chip2", "label": "माफी मांगें", "philosophy": "गलती मानना बड़प्पन है"},
                    {"id": "chip3", "label": "समाधान दें", "philosophy": "समाधान से भरोसा बनता है"}
                ],
                "success_criteria": ["शिकायत का समाधान", "सुपरवाइज़र का भरोसा बनाए रखें"],
                "rubric": {"communication": 60, "composure": 45, "clarity": 65, "strategy": 50, "outcome": 45},
                "transfer_targets": ["ग्राहक सेवा", "समस्या समाधान"]
            }
        }
    
    def get_template_key(self, input_data):
        """Generate template key from input"""
        icp = input_data.get("icp_type")
        milestone = input_data.get("milestone_code", "M01")
        skill = input_data.get("skill_target", "communication")
        lang = input_data.get("language", "en")
        
        # Simplify skill for template matching
        skill_simple = skill.replace("_", "").lower()
        
        return f"{icp}_{milestone}_{skill_simple}_{lang}"
    
    def generate_scenario(self, input_data):
        """Return pre-defined template (100% consistent)"""
        template_key = self.get_template_key(input_data)
        
        # Try exact match
        if template_key in self.templates:
            return self.templates[template_key]
        
        # Try fallback to default template
        icp = input_data.get("icp_type")
        lang = input_data.get("language", "en")
        fallback_key = f"{icp}_M01_communication_{lang}"
        
        if fallback_key in self.templates:
            return self.templates[fallback_key]
        
        # Ultimate fallback
        return self.get_default_scenario(icp, lang)
    
    def get_default_scenario(self, icp_type, language):
        """Return default scenario"""
        if icp_type == "high_wage":
            return self.templates["high_wage_M01_communication_en"]
        else:
            return self.templates["low_wage_M01_customer_handling_hi"]

# Use this in your api.py
# from template_writer import TemplateScenarioWriter
# writer = TemplateScenarioWriter()  # Instead of ScenarioWriter()