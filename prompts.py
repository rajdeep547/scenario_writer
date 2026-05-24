SYSTEM_PROMPT = """You are an expert scenario writer. Generate DIFFERENT scenarios for DIFFERENT skills.

CRITICAL RULE: The skill_target determines EVERYTHING in the scenario.

For EACH different skill_target, you MUST create a COMPLETELY DIFFERENT scenario:
- Different setting
- Different antagonist line  
- Different characters
- Different strategies
- Different success criteria

If skill_target = "negotiation" → create a salary/contract negotiation scenario
If skill_target = "public_speaking" → create a presentation/pitch scenario
If skill_target = "time_management" → create a deadline/priority scenario
If skill_target = "customer_service" → create a complaint handling scenario
If skill_target = "technical_writing" → create a documentation scenario
If skill_target = "leadership" → create a team management scenario
If skill_target = "conflict_resolution" → create a dispute scenario
If skill_target = "teamwork" → create a collaboration scenario

Output ONLY valid JSON, no other text.

Output format:
{
  "scene": {"setting": "...", "time": "...", "context": "..."},
  "characters": [{"name": "...", "role": "...", "mood": "..."}],
  "antagonist_opening_line": "...",
  "strategy_chips": [
    {"id": "chip1", "label": "...", "philosophy": "..."},
    {"id": "chip2", "label": "...", "philosophy": "..."},
    {"id": "chip3", "label": "...", "philosophy": "..."}
  ],
  "success_criteria": ["...", "...", "..."],
  "rubric": {"communication": 0-100, "composure": 0-100, "clarity": 0-100, "strategy": 0-100, "outcome": 0-100},
  "transfer_targets": ["...", "..."]
}"""

def build_user_prompt(icp_type, milestone_code, skill_target, language):
    # Different instructions based on skill_target
    skill_specific_instructions = {
        "negotiation": """
Create a salary negotiation scenario where the employee must negotiate a raise or promotion.
Setting: HR office or manager's cabin.
Antagonist: Manager saying budget is tight.
Strategies: Prepare market research, highlight achievements, ask for growth path.
""",
        "public_speaking": """
Create a presentation scenario where the employee must present to senior leadership.
Setting: Conference room with executives.
Antagonist: Tough audience asking difficult questions.
Strategies: Practice beforehand, use storytelling, handle Q&A confidently.
""",
        "time_management": """
Create a deadline management scenario with multiple competing priorities.
Setting: Busy office with urgent tasks.
Antagonist: Manager adding more work.
Strategies: Prioritize tasks, delegate, communicate timeline clearly.
""",
        "customer_service": """
Create a customer complaint scenario where a customer is angry.
Setting: Customer service desk or phone call.
Antagonist: Angry customer demanding resolution.
Strategies: Listen actively, apologize sincerely, offer solution.
""",
        "technical_writing": """
Create a documentation scenario where code needs documentation.
Setting: Software development team.
Antagonist: Tech lead saying documentation is missing.
Strategies: Write clearly, use examples, review with team.
""",
        "leadership": """
Create a team motivation scenario where team morale is low.
Setting: Team meeting room.
Antagonist: Disengaged team members.
Strategies: Recognize achievements, set clear goals, provide support.
""",
        "conflict_resolution": """
Create a team conflict scenario between two colleagues.
Setting: Meeting room with conflicting parties.
Antagonist: Angry colleague blaming others.
Strategies: Mediate calmly, find common ground, focus on solutions.
""",
        "teamwork": """
Create a collaboration scenario where team members aren't cooperating.
Setting: Project workspace.
Antagonist: Team member not sharing information.
Strategies: Communicate openly, divide tasks fairly, build trust.
"""
    }
    
    # Get specific instruction or default
    skill_lower = skill_target.lower().replace("_", " ").strip()
    specific_instruction = skill_specific_instructions.get(
        skill_lower.split()[0] if skill_lower.split() else skill_lower,
        f"""
Create a scenario specifically about practicing "{skill_target}".
The entire scenario must focus on this skill.
The antagonist line must directly mention needing to improve "{skill_target}".
The strategies must teach how to master "{skill_target}".
"""
    )
    
    if icp_type == "high_wage":
        context = "Tech office, software company, IT professional environment"
        characters = "Software engineers, tech leads, product managers"
    else:
        context = "Customer service center, small office, entry-level workplace"
        characters = "Supervisors, team leads, customer service representatives"
    
    if language == "hi":
        lang_text = "Hindi (Devanagari script)"
    else:
        lang_text = "English"
    
    return f"""
SKILL TARGET: {skill_target} (THIS IS THE MOST IMPORTANT - Create scenario for THIS SPECIFIC SKILL)

Context: {context}
Characters: {characters}
Language: {lang_text}
Milestone: {milestone_code}

{specific_instruction}

IMPORTANT: The scenario MUST be DIFFERENT for each skill_target.
DO NOT generate the same scenario for different skills.

Generate the scenario JSON now:"""