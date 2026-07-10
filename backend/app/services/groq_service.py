import json
import re

from groq import Groq

from app.config import settings
from app.schemas.scenario import ScenarioContent, ScenarioGenerateRequest

DIFFICULTY_LABELS = {
    "M01": "Beginner",
    "M02": "Elementary",
    "M03": "Intermediate",
    "M04": "Upper Intermediate",
    "M05": "Advanced",
    "M06": "Proficient",
    "M07": "Expert",
}

LANGUAGE_LABELS = {
    "en": "English",
    "hi": "Hindi (Devanagari script)",
}


def _build_prompt(request: ScenarioGenerateRequest) -> str:
    difficulty_label = DIFFICULTY_LABELS[request.difficulty]
    language_label = LANGUAGE_LABELS[request.language]

    return f"""You are an expert Indian scenario designer for skill-based training simulations.

Create a realistic, immersive scenario for the skill: "{request.skill_target}"
Difficulty level: {request.difficulty} ({difficulty_label})
Language: {language_label}

Requirements:
- Set the scene in a real Indian location with specific time and context
- Use Indian character names with realistic emotions and roles
- Include one tense antagonist dialogue line that creates pressure
- Provide exactly 3 strategy chips with label, approach, and explanation
- Provide exactly 5 rubric items with criterion, score (1-5), and description
- Provide 3-5 measurable success criteria
- Provide 3-5 real-world transfer targets (skills learned)

{"Write ALL text content in Hindi using Devanagari script." if request.language == "hi" else "Write ALL text content in English."}

Return ONLY valid JSON with this exact structure (no markdown, no extra text):
{{
  "scene": "detailed scene description",
  "characters": ["character 1 with role and emotion", "character 2..."],
  "antagonist_line": "tense dialogue line",
  "strategy_chips": [
    {{"label": "short label", "approach": "what to do", "explanation": "why it works"}}
  ],
  "rubric": [
    {{"criterion": "name", "score": 4, "description": "what good looks like"}}
  ],
  "success_criteria": ["measurable outcome 1"],
  "transfer_targets": ["real-world skill 1"]
}}"""


def _extract_json(raw: str) -> dict:
    text = raw.strip()
    fence_match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if fence_match:
        text = fence_match.group(1).strip()
    return json.loads(text)


class GroqService:
    def __init__(self) -> None:
        self.client = Groq(api_key=settings.groq_api_key)

    def generate_scenario(self, request: ScenarioGenerateRequest) -> ScenarioContent:
        if not settings.groq_api_key:
            raise ValueError("GROQ_API_KEY is not configured")

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a JSON-only scenario generator. Always return valid JSON.",
                },
                {"role": "user", "content": _build_prompt(request)},
            ],
            temperature=0.8,
            max_tokens=4096,
        )

        raw_content = response.choices[0].message.content or ""
        parsed = _extract_json(raw_content)
        return ScenarioContent.model_validate(parsed)


groq_service = GroqService()
