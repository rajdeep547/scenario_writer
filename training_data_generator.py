import json
import random

class TrainingDataGenerator:
    """Generate consistent training data for fine-tuning"""
    
    def __init__(self):
        self.scenario_patterns = {
            "high_wage": {
                "settings": [
                    "Bangalore tech park, meeting room",
                    "Startup office, open workspace",
                    "Product team standup area",
                    "Client conference room"
                ],
                "characters": {
                    "tech_lead": ["Priya", "Rajesh", "Arjun", "Neha"],
                    "developer": ["Rahul", "Sneha", "Vikram", "Anjali"],
                    "manager": ["Deepak", "Kavita", "Sanjay", "Meera"]
                },
                "tensions": [
                    "missed deadline",
                    "code quality issue",
                    "client escalation",
                    "team conflict"
                ]
            },
            "low_wage": {
                "settings": [
                    "Customer support center",
                    "Delivery hub office",
                    "Small business office",
                    "Training room"
                ],
                "characters": {
                    "supervisor": ["Priya", "Rajesh", "Neha", "Sanjay"],
                    "worker": ["Arjun", "Sunita", "Ramesh", "Kavita"],
                    "customer": ["Mr. Sharma", "Mrs. Gupta", "Client", "Vendor"]
                },
                "tensions": [
                    "customer complaint",
                    "delivery delay",
                    "system error",
                    "miscommunication"
                ]
            }
        }
    
    def generate_consistent_scenario(self, icp_type, milestone, skill, language):
        """Generate consistent scenario based on patterns"""
        
        pattern = self.scenario_patterns[icp_type]
        
        # Consistent selection based on input (not random)
        # Using hash of input to ensure same input = same selection
        hash_value = hash(f"{icp_type}_{milestone}_{skill}_{language}") % 100
        
        setting_idx = hash_value % len(pattern["settings"])
        tension_idx = (hash_value // 10) % len(pattern["tensions"])
        
        scenario = {
            "scene": {
                "setting": pattern["settings"][setting_idx],
                "time": self.get_time(hash_value),
                "context": self.get_context(tension_idx, pattern["tensions"])
            },
            "characters": self.get_characters(icp_type, hash_value),
            "antagonist_opening_line": self.get_antagonist_line(
                icp_type, tension_idx, hash_value
            ),
            "strategy_chips": self.get_strategy_chips(hash_value),
            "success_criteria": self.get_success_criteria(icp_type, milestone),
            "rubric": self.get_rubric(milestone),
            "transfer_targets": self.get_transfer_targets(skill, language)
        }
        
        return scenario
    
    def get_time(self, seed):
        times = ["9:00 AM", "10:30 AM", "2:00 PM", "4:30 PM", "5:00 PM"]
        return times[seed % len(times)]
    
    def get_context(self, idx, tensions):
        return f"You are facing a {tensions[idx]} situation"
    
    def get_characters(self, icp_type, seed):
        pattern = self.scenario_patterns[icp_type]
        if icp_type == "high_wage":
            return [
                {"name": pattern["characters"]["tech_lead"][seed % len(pattern["characters"]["tech_lead"])], 
                 "role": "Tech Lead", "mood": "frustrated"},
                {"name": pattern["characters"]["developer"][(seed + 1) % len(pattern["characters"]["developer"])], 
                 "role": "Developer", "mood": "stressed"}
            ]
        else:
            return [
                {"name": pattern["characters"]["supervisor"][seed % len(pattern["characters"]["supervisor"])], 
                 "role": "Supervisor", "mood": "serious"},
                {"name": pattern["characters"]["worker"][(seed + 1) % len(pattern["characters"]["worker"])], 
                 "role": "Worker", "mood": "anxious"}
            ]
    
    def get_antagonist_line(self, icp_type, tension_idx, seed):
        if icp_type == "high_wage":
            lines = [
                "Your feature is 2 days late. The client demo is tomorrow.",
                "The code you pushed broke the production environment.",
                "The client escalated your work quality to senior management.",
                "Your teammate is frustrated with your communication style."
            ]
        else:
            lines = [
                "A customer complained about your service today.",
                "You missed the delivery deadline for the 3rd time.",
                "The system shows you logged in late for your shift.",
                "Your supervisor wants to discuss your performance."
            ]
        return lines[tension_idx % len(lines)]
    
    def get_strategy_chips(self, seed):
        strategies = [
            [
                {"id": "chip1", "label": "Take responsibility", 
                 "philosophy": "Ownership builds trust"},
                {"id": "chip2", "label": "Propose solution", 
                 "philosophy": "Action shows commitment"},
                {"id": "chip3", "label": "Seek guidance", 
                 "philosophy": "Collaboration solves problems"}
            ],
            [
                {"id": "chip1", "label": "Apologize sincerely", 
                 "philosophy": "Apology acknowledges impact"},
                {"id": "chip2", "label": "Explain situation", 
                 "philosophy": "Context helps understanding"},
                {"id": "chip3", "label": "Offer improvement plan", 
                 "philosophy": "Plan shows seriousness"}
            ]
        ]
        return strategies[seed % len(strategies)]
    
    def get_success_criteria(self, icp_type, milestone):
        if icp_type == "high_wage":
            return [
                "Resolve the technical issue",
                "Maintain team relationships",
                "Meet revised deadline"
            ]
        else:
            return [
                "Address customer concern",
                "Follow proper process",
                "Learn from feedback"
            ]
    
    def get_rubric(self, milestone):
        # Scores decrease as milestone increases (harder scenarios)
        base_score = 80 - (int(milestone[1:]) * 5)
        return {
            "communication": max(20, base_score),
            "composure": max(20, base_score - 5),
            "clarity": max(20, base_score + 5),
            "strategy": max(20, base_score - 10),
            "outcome": max(20, base_score - 15)
        }
    
    def get_transfer_targets(self, skill, language):
        return [skill.replace("_", " "), "workplace communication"]

# Usage
if __name__ == "__main__":
    generator = TrainingDataGenerator()
    
    # Same input always produces same output
    result1 = generator.generate_consistent_scenario("high_wage", "M03", "communication", "en")
    result2 = generator.generate_consistent_scenario("high_wage", "M03", "communication", "en")
    
    print(f"Outputs are identical: {result1 == result2}")