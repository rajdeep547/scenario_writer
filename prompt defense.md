# Prompt Defense Document

## 1. System Prompt Design Decisions

### Why this structure?
- **Rules first, examples later** - Models follow constraints better when stated upfront
- **Explicit auto-fail conditions** - Prevents common failure modes identified in rubric
- **ICP injection** - Forces model to differentiate between user types

### What I tried first:
- Single generic prompt for all cases → FAILED (low_wage got tech jargon)
- No philosophy field → FAILED (chips just repeated labels)
- Generic antagonist examples → FAILED (lines were boring)

### What broke and how I fixed:
| Problem | Fix |
|---------|-----|
| Similar strategy chips | Added "must be different" and validation |
| Generic antagonist lines | Required name + situation + consequence |
| Hindi had grammar issues | Added "Devanagari script" explicitly |

## 2. ICP Differentiation Strategy

### How outputs differ:

| Field | High_wage | Low_wage |
|-------|-----------|----------|
| Setting | Tech office | Customer center |
| Characters | Engineer, Tech Lead | Delivery partner, Supervisor |
| Language | Technical terms | Simple vocabulary |

## 3. Live Change Predictions

### If language changes from "en" to "hi":
- All text becomes Hindi
- Character names stay same (Indian names work for both)
- Antagonist line uses respectful forms

### If icp_type changes:
- Entire workplace context switches
- Vocabulary complexity drops
- Tension type changes (tech debt → customer complaint)

## 4. Failure Handling

### Edge cases covered:
- Missing fields → default values
- API failure → fallback scenarios (hardcoded valid JSON)
- Invalid milestone → defaults to M03
- Hallucinated fields → JSON extractor filters extras