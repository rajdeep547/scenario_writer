import google.generativeai as genai
import json
import re
import random
from config import GEMINI_API_KEY, MODEL_NAME
from prompts import SYSTEM_PROMPT, build_user_prompt

class ScenarioWriter:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not found in .env file")
        
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Use higher temperature for variety
        self.generation_config = {
            "temperature": 0.8,  # Higher for more variety
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        }
        
        self.model = genai.GenerativeModel(
            MODEL_NAME,
            system_instruction=SYSTEM_PROMPT,
            generation_config=self.generation_config
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
        
        print(f"🎯 Generating scenario for: {skill_target}")
        
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
            print(f"Error: {e}")
            # Return skill-specific fallback
            return self._get_skill_specific_fallback(icp_type, skill_target, language)
    
    def _extract_json(self, text):
        text = re.sub(r'```json\s*', '', text)
        text = re.sub(r'```\s*', '', text)
        
        start = text.find('{')
        end = text.rfind('}')
        
        if start == -1 or end == -1:
            raise ValueError("No JSON object found")
        
        json_str = text[start:end+1]
        return json.loads(json_str)
    
    def _validate_schema(self, output):
        required = ["scene", "characters", "antagonist_opening_line", 
                    "strategy_chips", "success_criteria", "rubric", "transfer_targets"]
        for field in required:
            if field not in output:
                raise ValueError(f"Missing {field}")
    
    def _get_skill_specific_fallback(self, icp_type, skill_target, language):
        """Return different outputs for different skills"""
        is_hindi = language == "hi"
        skill_lower = skill_target.lower()
        
        # Negotiation scenario
        if "negotiation" in skill_lower:
            if is_hindi:
                return {
                    "scene": {"setting": "एचआर कार्यालय", "time": "दोपहर 2 बजे", "context": "सैलरी नेगोशिएशन के लिए बुलाया गया"},
                    "characters": [{"name": "श्री शर्मा", "role": "एचआर मैनेजर", "mood": "पेशेवर"}, {"name": "राहुल", "role": "कर्मचारी", "mood": "उत्सुक"}],
                    "antagonist_opening_line": "राहुल, आपकी सैलरी बढ़ाने का समय आ गया है, लेकिन बजट सीमित है। आप क्यों बताएंगे कि बढ़ोतरी मिलनी चाहिए?",
                    "strategy_chips": [
                        {"id": "chip1", "label": "मार्केट रिसर्च दिखाएं", "philosophy": "डेटा से बात मजबूत होती है"},
                        {"id": "chip2", "label": "अपनी उपलब्धियां गिनाएं", "philosophy": "वैल्यू दिखाना जरूरी है"},
                        {"id": "chip3", "label": "ग्रोथ प्लान पूछें", "philosophy": "भविष्य पर फोकस करें"}
                    ],
                    "success_criteria": ["सैलरी बढ़ोतरी मिले", "साल भर में प्रमोशन का रास्ता बने"],
                    "rubric": {"communication": 75, "composure": 80, "clarity": 70, "strategy": 85, "outcome": 70},
                    "transfer_targets": ["negotiation", "salary discussion", "self advocacy"]
                }
            else:
                return {
                    "scene": {"setting": "HR Office", "time": "2 PM", "context": "Called for salary negotiation meeting"},
                    "characters": [{"name": "Mr. Sharma", "role": "HR Manager", "mood": "professional"}, {"name": "Rahul", "role": "Employee", "mood": "eager"}],
                    "antagonist_opening_line": "Rahul, it's time for your salary review. Budget is tight. Why should we give you a raise?",
                    "strategy_chips": [
                        {"id": "chip1", "label": "Show market research", "philosophy": "Data strengthens your case"},
                        {"id": "chip2", "label": "Highlight achievements", "philosophy": "Show the value you bring"},
                        {"id": "chip3", "label": "Ask for growth path", "philosophy": "Focus on future potential"}
                    ],
                    "success_criteria": ["Get salary increase", "Establish path for promotion"],
                    "rubric": {"communication": 75, "composure": 80, "clarity": 70, "strategy": 85, "outcome": 70},
                    "transfer_targets": ["negotiation", "salary discussion", "self advocacy"]
                }
        
        # Public Speaking scenario
        elif "public" in skill_lower or "speaking" in skill_lower or "presentation" in skill_lower:
            return {
                "scene": {"setting": "Conference room with 10 executives", "time": "9 AM", "context": "Quarterly business review presentation"},
                "characters": [{"name": "CEO", "role": "Chief Executive Officer", "mood": "serious"}, {"name": "Riya", "role": "Project Lead", "mood": "nervous"}],
                "antagonist_opening_line": "Riya, you have 10 minutes to present your project. Make it compelling. The board is watching.",
                "strategy_chips": [
                    {"id": "chip1", "label": "Start with impact", "philosophy": "First 30 seconds determine attention"},
                    {"id": "chip2", "label": "Use storytelling", "philosophy": "Stories are more memorable than data"},
                    {"id": "chip3", "label": "Handle Q&A confidently", "philosophy": "Difficult questions show your expertise"}
                ],
                "success_criteria": ["Audience engagement", "Clear key messages delivered", "Positive feedback received"],
                "rubric": {"communication": 80, "composure": 65, "clarity": 75, "strategy": 70, "outcome": 75},
                "transfer_targets": ["public speaking", "presentation skills", "audience engagement"]
            }
        
        # Time Management scenario
        elif "time" in skill_lower or "deadline" in skill_lower:
            return {
                "scene": {"setting": "Open office workspace", "time": "4:30 PM, Friday", "context": "Three deadlines all due tomorrow"},
                "characters": [{"name": "Manager", "role": "Team Lead", "mood": "stressed"}, {"name": "Arjun", "role": "Developer", "mood": "overwhelmed"}],
                "antagonist_opening_line": "Arjun, we have three clients expecting delivery tomorrow. What's your plan to get everything done?",
                "strategy_chips": [
                    {"id": "chip1", "label": "Prioritize tasks", "philosophy": "Not everything is equally important"},
                    {"id": "chip2", "label": "Delegate where possible", "philosophy": "You don't have to do everything"},
                    {"id": "chip3", "label": "Communicate realistic timeline", "philosophy": "Better to be honest than fail"}
                ],
                "success_criteria": ["All critical tasks completed", "Stakeholders informed", "No burnout"],
                "rubric": {"communication": 65, "composure": 55, "clarity": 70, "strategy": 75, "outcome": 65},
                "transfer_targets": ["time management", "prioritization", "deadline management"]
            }
        
        # Customer Service scenario
        elif "customer" in skill_lower or "service" in skill_lower:
            return {
                "scene": {"setting": "Customer support call center", "time": "6 PM, busy hour", "context": "Angry customer on line"},
                "characters": [{"name": "Customer", "role": "Client", "mood": "furious"}, {"name": "Priya", "role": "Support Agent", "mood": "anxious"}],
                "antagonist_opening_line": "I've been waiting for 30 minutes! Your company is useless. Fix my problem NOW!",
                "strategy_chips": [
                    {"id": "chip1", "label": "Listen actively", "philosophy": "Let them vent first"},
                    {"id": "chip2", "label": "Apologize sincerely", "philosophy": "Acknowledge their frustration"},
                    {"id": "chip3", "label": "Offer solution", "philosophy": "Focus on what you CAN do"}
                ],
                "success_criteria": ["Customer calms down", "Issue resolved", "Customer retention"],
                "rubric": {"communication": 70, "composure": 60, "clarity": 65, "strategy": 70, "outcome": 65},
                "transfer_targets": ["customer service", "conflict resolution", "empathy"]
            }
        
        # Technical Writing scenario
        elif "technical" in skill_lower or "writing" in skill_lower or "documentation" in skill_lower:
            return {
                "scene": {"setting": "Development team workspace", "time": "11 AM", "context": "API documentation missing"},
                "characters": [{"name": "Tech Lead", "role": "Senior Developer", "mood": "frustrated"}, {"name": "Rahul", "role": "Junior Developer", "mood": "confused"}],
                "antagonist_opening_line": "Rahul, your API has no documentation. Other teams are blocked. When can we expect proper docs?",
                "strategy_chips": [
                    {"id": "chip1", "label": "Write clear examples", "philosophy": "Examples explain better than text"},
                    {"id": "chip2", "label": "Use consistent format", "philosophy": "Consistency reduces confusion"},
                    {"id": "chip3", "label": "Get peer review", "philosophy": "Fresh eyes catch mistakes"}
                ],
                "success_criteria": ["Complete documentation", "Team understands API", "No more blocking"],
                "rubric": {"communication": 70, "composure": 65, "clarity": 80, "strategy": 70, "outcome": 75},
                "transfer_targets": ["technical writing", "documentation", "knowledge sharing"]
            }
        
        # Default - Generic but skill-specific
        else:
            return {
                "scene": {"setting": "Professional workplace", "time": "Mid-day", "context": f"Need to demonstrate {skill_target} skills"},
                "characters": [{"name": "Manager", "role": "Supervisor", "mood": "attentive"}, {"name": "Employee", "role": "Team Member", "mood": "focused"}],
                "antagonist_opening_line": f"Show me how you would handle this {skill_target} situation",
                "strategy_chips": [
                    {"id": "chip1", "label": f"Analyze the {skill_target} need", "philosophy": "Understanding is first step"},
                    {"id": "chip2", "label": f"Apply {skill_target} best practices", "philosophy": "Proven methods work"},
                    {"id": "chip3", "label": f"Get feedback on {skill_target}", "philosophy": "Improvement requires input"}
                ],
                "success_criteria": [f"Demonstrate {skill_target}", f"Get positive {skill_target} evaluation", "Build confidence"],
                "rubric": {"communication": 65, "composure": 60, "clarity": 70, "strategy": 65, "outcome": 60},
                "transfer_targets": [skill_target, "professional development", "workplace success"]
            }