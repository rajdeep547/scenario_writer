SYSTEM_PROMPT = """You are an expert scenario writer for a career upskilling platform. 
Your job: Generate realistic workplace scenarios based on user profiles.

CRITICAL RULES:
1. Output ONLY valid JSON - no extra text, no markdown formatting
2. The `antagonist_opening_line` must be specific, vivid, and create real tension - NOT generic like "I'm unhappy with your work"
3. The 3 `strategy_chips` must represent MEANINGFULLY DIFFERENT approaches (passive, assertive, collaborative, strategic, etc.)
4. Each chip's `philosophy` explains WHY that strategy works, not just WHAT to do
5. `rubric` scores must reflect genuine differences based on scenario difficulty (not all 50s)
6. For `high_wage`: Technical workplace context, professional characters, software/IT settings
7. For `low_wage`: Customer service/gig contexts, accessible language, confidence-building scenarios
8. For `language: "hi"`: Output ALL text fields in Hindi (Devanagari script)

Output JSON structure:
{
  "scene": {"setting": "specific location", "time": "time of day/context", "context": "what led to this moment"},
  "characters": [{"name": "Indian name", "role": "job title", "mood": "emotional state"}],
  "antagonist_opening_line": "specific, tense dialogue line",
  "strategy_chips": [
    {"id": "chip1", "label": "short action label", "philosophy": "why this works psychologically/strategically"},
    {"id": "chip2", "label": "...", "philosophy": "..."},
    {"id": "chip3", "label": "...", "philosophy": "..."}
  ],
  "success_criteria": ["specific outcome 1", "specific outcome 2", "specific outcome 3"],
  "rubric": {"communication": 0-100, "composure": 0-100, "clarity": 0-100, "strategy": 0-100, "outcome": 0-100},
  "transfer_targets": ["real-world skill 1", "real-world skill 2"]
}"""

def build_user_prompt(icp_type, episode_title, milestone_code, skill_target, language):
    if icp_type == "high_wage":
        context_guide = """
CONTEXT: HIGH-WAGE USER (Engineering student → Software Engineer)
- Setting: Tech office, startup, product team, standup meetings, code review
- Characters: Tech lead, product manager, senior dev, HR, CEO
- Tension types: Missed deadlines, technical debt, communication breakdown, feature scope creep
- Antagonist style: Professional pressure, subtle criticism, team expectations
"""
    else:
        context_guide = """
CONTEXT: LOW-WAGE USER (Gig worker → Data entry / office job)
- Setting: Customer support center, small office, training room, team meeting
- Characters: Supervisor, senior colleague, customer, HR person, team lead
- Tension types: Customer complaint, performance pressure, learning new software, time management
- Antagonist style: Direct but not cruel, practical pressure, expectations with support
"""
    
    if language == "hi":
        lang_instruction = "IMPORTANT: Generate ALL output text in Hindi (Devanagari script). Use proper Hindi vocabulary and sentence structure."
    else:
        lang_instruction = "Generate output in English"
    
    return f"""{context_guide}
{lang_instruction}

Now generate a scenario with these parameters:
- ICP Type: {icp_type}
- Episode Title: {episode_title}
- Milestone Code: {milestone_code}
- Skill Target: {skill_target}

Remember:
1. antagonist_opening_line must be SPECIFIC (include names, situations, consequences)
2. Three strategy_chips must be genuinely different from each other
3. rubric scores must be logical (harder scenarios = lower scores, but not all 50)
4. For Hindi output, ensure proper Devanagari script

Output ONLY valid JSON, no other text."""