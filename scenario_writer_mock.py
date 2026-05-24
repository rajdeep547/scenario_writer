import json
import hashlib

class ScenarioWriter:
    """Intelligent Scenario Writer - DIFFERENT scenarios for High Wage vs Low Wage"""
    
    def __init__(self):
        print("✅ Intelligent Scenario Writer initialized")
        self._init_scenario_templates()
    
    def _init_scenario_templates(self):
        """Initialize scenario templates for different skill categories"""
        
        # ========== HIGH WAGE - Tech/Professional Scenarios ==========
        self.high_wage_scenarios = {
            "coding": {
                "keywords": ["coding", "code", "programming", "development", "software"],
                "setting": "Tech startup office, sprint planning meeting",
                "characters": ["Senior Developer", "Junior Developer"],
                "context": "Code quality issues in production",
                "antagonist": "Your code broke production last night! 1000 users affected. Explain what happened and how you'll fix it.",
                "strategies": [
                    "Write unit tests before fixing",
                    "Do root cause analysis first",
                    "Create rollback plan before deployment"
                ],
                "philosophies": [
                    "Tests prevent regression and catch issues early.",
                    "Understanding why helps prevent recurrence.",
                    "Always have escape plan before making changes."
                ]
            },
            "debugging": {
                "keywords": ["debug", "debugging", "bug", "error", "issue", "fix"],
                "setting": "Production environment, critical outage war room",
                "characters": ["Tech Lead", "On-call Engineer"],
                "context": "Critical bug causing data loss",
                "antagonist": "Users are losing data! Every minute costs $10,000. Find the root cause NOW!",
                "strategies": [
                    "Check recent deployments first",
                    "Add detailed logging",
                    "Reproduce in staging"
                ],
                "philosophies": [
                    "80% of issues come from recent changes.",
                    "More data = faster root cause analysis.",
                    "Safe environment for testing without risk."
                ]
            },
            "api": {
                "keywords": ["api", "rest", "graphql", "endpoint", "microservice", "integration"],
                "setting": "Integration team meeting, whiteboard session",
                "characters": ["API Architect", "Integration Engineer"],
                "context": "Designing new microservice API",
                "antagonist": "Your API design has no rate limiting! How will it handle 10,000 requests per second? Redesign it!",
                "strategies": [
                    "Add rate limiting headers",
                    "Implement circuit breaker pattern",
                    "Use API gateway for throttling"
                ],
                "philosophies": [
                    "Protect backend from traffic spikes.",
                    "Fail fast, fail gracefully under load.",
                    "Centralize cross-cutting concerns."
                ]
            },
            "communication": {
                "keywords": ["communication", "communicate", "explain", "present", "talk"],
                "setting": "Cross-functional team meeting with stakeholders",
                "characters": ["Product Manager", "Engineering Lead"],
                "context": "Explaining technical debt to non-technical stakeholders",
                "antagonist": "The business team doesn't understand why refactoring is important. Explain technical debt without using jargon!",
                "strategies": [
                    "Use house renovation analogy",
                    "Show business impact of delay",
                    "Present cost-benefit analysis"
                ],
                "philosophies": [
                    "Compare to fixing foundation of house.",
                    "Connect technical work to business outcomes.",
                    "Show long-term savings vs short-term cost."
                ]
            },
            "leadership": {
                "keywords": ["leadership", "leader", "manage", "manager", "lead", "guide"],
                "setting": "Team retrospective meeting room",
                "characters": ["Engineering Manager", "Team Lead"],
                "context": "Team morale low after missed deadline",
                "antagonist": "Three team members want to quit. Project is 2 weeks behind. How will you motivate the team?",
                "strategies": [
                    "Acknowledge failure openly",
                    "Recognize individual efforts",
                    "Create achievable quick wins"
                ],
                "philosophies": [
                    "Leaders take responsibility, not blame.",
                    "People need to feel valued and seen.",
                    "Small successes rebuild confidence."
                ]
            },
            "presentation": {
                "keywords": ["presentation", "present", "pitch", "slide", "deck", "speak"],
                "setting": "Executive boardroom with large screen",
                "characters": ["CEO", "Product Head"],
                "context": "Quarterly business review presentation",
                "antagonist": "The board is skeptical about your project's ROI. Convince them to continue funding in 10 minutes!",
                "strategies": [
                    "Start with a powerful hook",
                    "Use data storytelling",
                    "Prepare for tough questions"
                ],
                "philosophies": [
                    "First 30 seconds determine attention span.",
                    "Numbers without context don't persuade.",
                    "Anticipate and address concerns proactively."
                ]
            },
            "negotiation": {
                "keywords": ["negotiation", "negotiate", "salary", "raise", "hike", "promotion"],
                "setting": "HR office, glass cabin",
                "characters": ["HR Manager", "Employee"],
                "context": "Annual salary review and promotion discussion",
                "antagonist": "Budget only allows 8% hike. You want 30%. Market data shows 15% is average. Why should we pay you premium?",
                "strategies": [
                    "Quantify your business impact",
                    "Present market research data",
                    "Negotiate total compensation package"
                ],
                "philosophies": [
                    "Show revenue generated or cost saved.",
                    "Industry standards create objective benchmark.",
                    "Consider bonus, stocks, vacation, and title."
                ]
            },
            "deadline": {
                "keywords": ["deadline", "time", "schedule", "priority", "urgent", "sprint"],
                "setting": "Sprint planning meeting room",
                "characters": ["Project Manager", "Tech Lead"],
                "context": "Multiple projects competing for same resources",
                "antagonist": "3 clients, 3 deadlines, 2 developers. All by Friday. What's your delivery strategy?",
                "strategies": [
                    "Prioritize by business value",
                    "Communicate trade-offs clearly",
                    "Negotiate realistic extensions"
                ],
                "philosophies": [
                    "Not all projects equally important to revenue.",
                    "Be transparent about capacity limitations.",
                    "Better to delay one than fail all three."
                ]
            },
            "planning": {
                "keywords": ["planning", "plan", "roadmap", "strategy", "quarterly"],
                "setting": "Quarterly planning session, large conference room",
                "characters": ["Product Director", "Engineering Lead"],
                "context": "Planning next quarter's roadmap",
                "antagonist": "CEO promised 10 features. Realistically we can deliver 6. How do you manage expectations?",
                "strategies": [
                    "Show effort vs value matrix",
                    "Propose phased delivery",
                    "Identify must-have vs nice-to-have"
                ],
                "philosophies": [
                    "Visualize trade-offs for stakeholders.",
                    "Deliver MVP first, rest later.",
                    "Define minimum viable product clearly."
                ]
            },
            "problem": {
                "keywords": ["problem", "solve", "solution", "crisis", "outage", "emergency"],
                "setting": "Crisis management war room",
                "characters": ["Incident Commander", "Technical Lead"],
                "context": "Major production outage affecting all users",
                "antagonist": "Site is completely down! Every minute of downtime costs $50,000. Solve this NOW!",
                "strategies": [
                    "Rollback recent deployment",
                    "Check infrastructure health",
                    "Implement emergency fix"
                ],
                "philosophies": [
                    "Last change is often the culprit.",
                    "Servers, databases, network all need checking.",
                    "Quick fix first, permanent solution later."
                ]
            },
            "decision": {
                "keywords": ["decision", "choose", "select", "architecture", "tech stack"],
                "setting": "Architecture review meeting",
                "characters": ["CTO", "Senior Architect"],
                "context": "Choosing between two competing technologies",
                "antagonist": "Team is split 50-50 on React vs Vue. You have to break the tie. How will you decide?",
                "strategies": [
                    "Create evaluation matrix",
                    "Build small prototype in both",
                    "Consider team expertise"
                ],
                "philosophies": [
                    "Score each option on objective criteria.",
                    "Test before committing to big decision.",
                    "Choose what team knows best for speed."
                ]
            },
            "review": {
                "keywords": ["review", "code review", "pr", "pull request", "feedback"],
                "setting": "Code review session, pair programming setup",
                "characters": ["Senior Reviewer", "Developer"],
                "context": "Critical pull request review before release",
                "antagonist": "Your PR has 15 comments and 8 requested changes. The release is tomorrow. How do you handle this feedback?",
                "strategies": [
                    "Prioritize critical fixes first",
                    "Schedule quick sync for clarification",
                    "Document decisions for future"
                ],
                "philosophies": [
                    "Fix security and bugs before style.",
                    "Video call faster than back-and-forth comments.",
                    "Write down why for future reference."
                ]
            }
        }
        
        # ========== LOW WAGE - Service/Gig Scenarios with keywords ==========
        self.low_wage_scenarios = {
            "customer_complaint": {
                "keywords": ["customer", "complaint", "angry", "upset", "unhappy", "dissatisfied", "irritated", "frustrated"],
                "setting": "Customer support center, open floor plan",
                "characters": ["Support Agent", "Angry Customer"],
                "context": "Customer complaint call about delayed order",
                "antagonist": "I've been waiting for 30 minutes! My order is 15 days late! Your service is terrible! Fix it NOW!",
                "strategies": [
                    "Apologize sincerely first",
                    "Listen without interrupting",
                    "Offer immediate solution"
                ],
                "philosophies": [
                    "Genuine apology reduces anger by 50%.",
                    "Let them vent completely before speaking.",
                    "Refund, discount, or expedited shipping."
                ]
            },
            "retention": {
                "keywords": ["retention", "loyalty", "churn", "leaving", "competitor", "stay"],
                "setting": "Call center floor, busy afternoon",
                "characters": ["Senior Agent", "Frustrated Customer"],
                "context": "Customer threatening to leave to competitor",
                "antagonist": "I'm taking my business elsewhere! Your competitor gives better service. Why should I stay?",
                "strategies": [
                    "Acknowledge their frustration",
                    "Explain what went wrong",
                    "Offer retention discount"
                ],
                "philosophies": [
                    "Validation calms angry customers.",
                    "Transparency about mistakes builds trust.",
                    "Sometimes discount is cheaper than losing customer."
                ]
            },
            "product_help": {
                "keywords": ["product", "help", "assist", "support", "issue", "problem", "not working"],
                "setting": "Service desk, retail store",
                "characters": ["Service Executive", "Client"],
                "context": "Customer needs help with product not working",
                "antagonist": "This product doesn't work as shown in the ad! I feel cheated! Either fix it or refund my money!",
                "strategies": [
                    "Show empathy first",
                    "Explain product features clearly",
                    "Offer exchange or refund"
                ],
                "philosophies": [
                    "Acknowledge their disappointment before solving.",
                    "Maybe they don't know how to use it.",
                    "Customer satisfaction worth more than one sale."
                ]
            },
            "delivery_pressure": {
                "keywords": ["delivery", "deliver", "order", "dispatch", "shipment", "rider", "logistics"],
                "setting": "Delivery hub, early morning rush",
                "characters": ["Hub Manager", "Delivery Partner"],
                "context": "Peak hour delivery pressure with short staff",
                "antagonist": "20 orders in 3 hours! 2 boys didn't come today! If we miss SLA, we lose client bonus! Can you handle it?",
                "strategies": [
                    "Plan optimal route first",
                    "Communicate realistic timeline",
                    "Ask other hubs for help"
                ],
                "philosophies": [
                    "Group nearby deliveries to save time.",
                    "Better to say 4 hours than fail in 3.",
                    "Teamwork across locations saves the day."
                ]
            },
            "warehouse_coordination": {
                "keywords": ["warehouse", "inventory", "stock", "loading", "packing", "shipment", "logistics"],
                "setting": "Warehouse floor, packed with boxes",
                "characters": ["Operations Lead", "Warehouse Staff"],
                "context": "Large shipment needs urgent processing",
                "antagonist": "500 boxes need loading in 2 hours! Team is confused, everyone doing different things! Take charge NOW!",
                "strategies": [
                    "Assign clear roles to everyone",
                    "Create assembly line process",
                    "Set small achievable targets"
                ],
                "philosophies": [
                    "Tell each person exactly what to do.",
                    "Divide tasks: loading, scanning, stacking.",
                    "50 boxes every 15 minutes builds momentum."
                ]
            },
            "dispatch_priority": {
                "keywords": ["dispatch", "assign", "prioritize", "schedule", "allocation", "task"],
                "setting": "Dispatch center, multiple screens",
                "characters": ["Dispatch Manager", "Field Agent"],
                "context": "Assigning tasks to field team with limited resources",
                "antagonist": "30 service requests came in overnight! Only 6 agents available. How will you prioritize and assign?",
                "strategies": [
                    "Categorize by urgency",
                    "Assign by location proximity",
                    "Match skills to task type"
                ],
                "philosophies": [
                    "Emergency requests first, then scheduled.",
                    "Group nearby tasks for same agent.",
                    "Experienced agents get complex tasks."
                ]
            },
            "patience_under_pressure": {
                "keywords": ["patience", "calm", "temper", "stress", "pressure", "frustration", "anger"],
                "setting": "Busy service center, long queue",
                "characters": ["Team Lead", "New Employee"],
                "context": "New employee struggling with difficult customer",
                "antagonist": "You look frustrated and about to lose temper. The customer is being unreasonable. How do you stay calm?",
                "strategies": [
                    "Take deep breaths",
                    "Remember it's not personal",
                    "Ask for break if needed"
                ],
                "philosophies": [
                    "Pause before responding calms the brain.",
                    "Customer angry at situation, not at you.",
                    "Short break better than saying wrong thing."
                ]
            },
            "team_collaboration": {
                "keywords": ["team", "together", "collaborate", "cooperate", "partner", "work together"],
                "setting": "Warehouse packing area, conveyor belt",
                "characters": ["Shift Supervisor", "Packers"],
                "context": "Team not cooperating, work piling up",
                "antagonist": "You two aren't talking! Orders are piling up! The faster packers are waiting for slower ones! How to fix this?",
                "strategies": [
                    "Redistribute workload evenly",
                    "Rotate tasks periodically",
                    "Set team-based target"
                ],
                "philosophies": [
                    "Balance work so everyone contributes fairly.",
                    "Everyone experiences all roles for empathy.",
                    "Reward team success, not individual speed."
                ]
            },
            "clear_communication": {
                "keywords": ["communication", "misunderstanding", "instruction", "clarify", "confusion"],
                "setting": "Team huddle, morning meeting",
                "characters": ["Supervisor", "Team Member"],
                "context": "Misunderstanding causing workflow issues",
                "antagonist": "You misunderstood the instruction again! Wrong items packed! Customer complaining! What happened and how to fix?",
                "strategies": [
                    "Repeat back instructions",
                    "Ask clarifying questions",
                    "Use written checklist"
                ],
                "philosophies": [
                    "Confirm understanding before starting.",
                    "Better to ask than make mistake.",
                    "Visual aid prevents forgetfulness."
                ]
            },
            "learning_new_skills": {
                "keywords": ["learning", "learn", "training", "new system", "new software", "skill"],
                "setting": "Training room, computer setup",
                "characters": ["Trainer", "Trainee"],
                "context": "New system rollout, employee struggling",
                "antagonist": "Everyone else learned the new system in 2 days. You're on day 5 and still making errors. What support do you need?",
                "strategies": [
                    "Ask for one-on-one training",
                    "Request written step-by-step guide",
                    "Practice after hours"
                ],
                "philosophies": [
                    "Individual attention for complex topics.",
                    "Reference document for future use.",
                    "Extra practice builds muscle memory."
                ]
            },
            "performance_improvement": {
                "keywords": ["improvement", "improve", "performance", "quality", "feedback", "review"],
                "setting": "Performance review meeting, small room",
                "characters": ["Manager", "Employee"],
                "context": "Quarterly performance review with quality issues",
                "antagonist": "Your speed is good but quality issues are increasing. 5 customer complaints this month. What's your improvement plan?",
                "strategies": [
                    "Ask for specific examples",
                    "Request additional training",
                    "Implement peer review process"
                ],
                "philosophies": [
                    "Understand exactly what went wrong.",
                    "Skill gap needs training investment.",
                    "Fresh eyes catch mistakes you miss."
                ]
            },
            "taking_initiative": {
                "keywords": ["initiative", "proactive", "suggestion", "improvement", "solution", "idea"],
                "setting": "Team meeting, whiteboard session",
                "characters": ["Supervisor", "Proactive Employee"],
                "context": "Process improvement opportunity identified",
                "antagonist": "You noticed we're wasting 2 hours daily on manual data entry. Management isn't asking, but you have a solution. Should you speak up?",
                "strategies": [
                    "Prepare solution proposal",
                    "Calculate time saved",
                    "Volunteer to implement"
                ],
                "philosophies": [
                    "Come with solution, not just problem.",
                    "Show business benefit in numbers.",
                    "Action builds credibility faster than words."
                ]
            },
            "billing_error": {
                "keywords": ["billing", "invoice", "payment", "charge", "money", "refund", "bill"],
                "setting": "Billing department, customer service desk",
                "characters": ["Billing Agent", "Angry Customer"],
                "context": "Customer disputing incorrect charge",
                "antagonist": "You charged me twice! I want my money back immediately! This is fraud! Fix it now or I'm complaining to the bank!",
                "strategies": [
                    "Apologize for error",
                    "Verify transaction details",
                    "Process refund immediately"
                ],
                "philosophies": [
                    "Accept mistake quickly builds trust.",
                    "Check records before promising action.",
                    "Fast refund > long explanation."
                ]
            },
            "return_policy": {
                "keywords": ["return", "refund", "exchange", "policy", "replacement", "defective"],
                "setting": "Returns counter, retail store",
                "characters": ["Returns Executive", "Customer"],
                "context": "Customer wants to return defective product",
                "antagonist": "The product stopped working after 2 days! Your return policy says 7 days. Why are you giving me trouble? Just take it back!",
                "strategies": [
                    "Check product condition",
                    "Explain policy politely",
                    "Offer exchange or store credit"
                ],
                "philosophies": [
                    "Verify before processing return.",
                    "Policy explained, not enforced rigidly.",
                    "Keep customer happy over small loss."
                ]
            },
            "escalation_handling": {
                "keywords": ["escalation", "supervisor", "manager", "higher authority", "complaint"],
                "setting": "Customer service supervisor desk",
                "characters": ["Team Lead", "Customer"],
                "context": "Customer demanding to speak to supervisor",
                "antagonist": "I want to speak to your manager! You're not helpful! Get me someone who can actually solve problems!",
                "strategies": [
                    "Stay calm and professional",
                    "Understand the real issue",
                    "Take ownership of resolution"
                ],
                "philosophies": [
                    "Don't take demand personally.",
                    "Often same solution needed.",
                    "Show authority to resolve."
                ]
            }
        }
    
    def generate_scenario(self, input_data):
        icp_type = input_data.get("icp_type", "high_wage")
        skill_target = input_data.get("skill_target", "communication")
        language = input_data.get("language", "en")
        milestone_code = input_data.get("milestone_code", "M03")
        
        print(f"🎯 Generating scenario for: {icp_type} | Skill: {skill_target}")
        
        # Choose database based on ICP type
        if icp_type == "high_wage":
            scenarios_db = self.high_wage_scenarios
            is_high_wage = True
        else:
            scenarios_db = self.low_wage_scenarios
            is_high_wage = False
        
        # Find matching scenario based on keywords
        skill_lower = skill_target.lower()
        matched_scenario = None
        matched_key = None
        
        # Search through scenarios to find keyword match
        for key, scenario in scenarios_db.items():
            if "keywords" in scenario:
                for keyword in scenario["keywords"]:
                    if keyword in skill_lower:
                        matched_scenario = scenario
                        matched_key = key
                        print(f"✅ Matched: '{skill_target}' with '{key}' (keyword: '{keyword}')")
                        break
                if matched_scenario:
                    break
        
        # If no keyword match, try partial match on key name
        if not matched_scenario:
            for key in scenarios_db:
                if key in skill_lower or skill_lower in key:
                    matched_scenario = scenarios_db[key]
                    matched_key = key
                    print(f"⚠️ Partial match: '{skill_target}' with '{key}'")
                    break
        
        # Use default if still no match
        if not matched_scenario:
            print(f"⚠️ No match found for '{skill_target}', using default")
            if is_high_wage:
                matched_scenario = {
                    "setting": "Tech office meeting room",
                    "characters": ["Manager", "Employee"],
                    "context": f"Need to demonstrate {skill_target} skills",
                    "antagonist": f"Show me how you handle {skill_target} in a professional setting.",
                    "strategies": [
                        "Analyze the situation carefully",
                        "Plan your approach before acting",
                        "Execute with confidence and clarity"
                    ],
                    "philosophies": [
                        "Understanding requirements is first step.",
                        "Preparation prevents poor performance.",
                        "Action without hesitation builds trust."
                    ]
                }
            else:
                matched_scenario = {
                    "setting": "Service center work area",
                    "characters": ["Supervisor", "Staff Member"],
                    "context": f"Opportunity to demonstrate {skill_target} skills",
                    "antagonist": f"Show me your {skill_target} skills in this real workplace situation.",
                    "strategies": [
                        "Listen carefully to understand the need",
                        "Respond with respect and patience",
                        "Focus on solving the actual problem"
                    ],
                    "philosophies": [
                        "Understanding needs before taking action.",
                        "Respect builds trust and cooperation.",
                        "Solution-focused mindset wins."
                    ]
                }
        
        # Calculate difficulty based on milestone
        difficulty_map = {
            "M01": 15, "M02": 10, "M03": 5, "M04": 0, "M05": -5, "M06": -10, "M07": -15
        }
        difficulty = difficulty_map.get(milestone_code, 0)
        
        # Generate unique seed for consistent output
        seed = hash(skill_target + icp_type) % 100
        
        # Build output
        output = {
            "scene": {
                "setting": matched_scenario["setting"],
                "time": self._get_time(seed),
                "context": matched_scenario["context"]
            },
            "characters": self._get_characters(matched_scenario["characters"], is_high_wage, seed),
            "antagonist_opening_line": matched_scenario["antagonist"],
            "strategy_chips": [
                {"id": f"chip{i+1}", "label": matched_scenario["strategies"][i], "philosophy": matched_scenario["philosophies"][i]}
                for i in range(3)
            ],
            "success_criteria": self._get_success_criteria(skill_target, is_high_wage, seed),
            "rubric": self._get_rubric(difficulty, seed),
            "transfer_targets": self._get_transfer_targets(skill_target, is_high_wage)
        }
        
        # Hindi translation if needed
        if language == "hi":
            output = self._to_hindi(output)
        
        return output
    
    def _get_time(self, seed):
        times = ["9:00 AM", "10:30 AM", "11:00 AM", "2:00 PM", "3:30 PM", "4:45 PM"]
        return times[seed % len(times)]
    
    def _get_characters(self, base_chars, is_high_wage, seed):
        if is_high_wage:
            names = ["Rajesh", "Priya", "Vikram", "Neha", "Arjun", "Meera"]
            roles = ["Tech Lead", "Product Manager", "Senior Developer", "Engineering Manager"]
        else:
            names = ["Ramesh", "Sunita", "Arjun", "Kavita", "Suresh", "Priya", "Manoj", "Geeta"]
            roles = ["Supervisor", "Team Leader", "Senior Agent", "Hub Manager", "Customer Lead", "Operations Head"]
        
        char1_name = names[seed % len(names)]
        char2_name = names[(seed + 3) % len(names)]
        char1_role = roles[seed % len(roles)]
        char2_role = roles[(seed + 2) % len(roles)]
        moods = ["focused", "determined", "calm", "prepared", "confident", "attentive"]
        
        return [
            {"name": char1_name, "role": base_chars[0] if len(base_chars) > 0 else char1_role, "mood": moods[seed % len(moods)]},
            {"name": char2_name, "role": base_chars[1] if len(base_chars) > 1 else char2_role, "mood": moods[(seed + 2) % len(moods)]}
        ]
    
    def _get_success_criteria(self, skill, is_high_wage, seed):
        if is_high_wage:
            return [
                f"Successfully demonstrate {skill} under pressure",
                "Receive positive feedback from stakeholders",
                "Document lessons learned for team"
            ]
        else:
            return [
                f"Complete task using {skill} effectively",
                "Customer or supervisor expresses satisfaction",
                "Identify areas for further improvement"
            ]
    
    def _get_rubric(self, difficulty, seed):
        base = 75 + difficulty
        return {
            "communication": max(20, min(95, base + (seed % 10) - 5)),
            "composure": max(20, min(95, base - 5 + (seed % 10) - 5)),
            "clarity": max(20, min(95, base + 5 + (seed % 10) - 5)),
            "strategy": max(20, min(95, base - 10 + (seed % 10) - 5)),
            "outcome": max(20, min(95, base - 15 + (seed % 10) - 5))
        }
    
    def _get_transfer_targets(self, skill, is_high_wage):
        if is_high_wage:
            return [skill, "Career Advancement", "Technical Excellence"]
        else:
            return [skill, "Workplace Success", "Customer Satisfaction"]
    
    def _to_hindi(self, output):
        return {
            "scene": {
                "setting": output["scene"]["setting"] + " (हिंदी)",
                "time": output["scene"]["time"],
                "context": output["scene"]["context"] + " - हिंदी में"
            },
            "characters": [
                {"name": c["name"], "role": c["role"] + " (हिंदी)", "mood": c["mood"]}
                for c in output["characters"]
            ],
            "antagonist_opening_line": output["antagonist_opening_line"] + " (हिंदी अनुवाद)",
            "strategy_chips": [
                {"id": chip["id"], "label": chip["label"] + " (हिंदी)", "philosophy": chip["philosophy"] + " (हिंदी)"}
                for chip in output["strategy_chips"]
            ],
            "success_criteria": [c + " (हिंदी)" for c in output["success_criteria"]],
            "rubric": output["rubric"],
            "transfer_targets": [t + " (हिंदी)" for t in output["transfer_targets"]]
        }


CachedScenarioWriter = ScenarioWriter
TemplateScenarioWriter = ScenarioWriter