# Practice Questions for Sanket

## Q1: What happens if I change language from "en" to "hi"?
**Answer:** All text fields become Hindi. Character names stay same. Antagonist line uses respectful forms. Philosophy translated to Hindi.

## Q2: What breaks if icp_type is wrong?
**Answer:** Low_wage user gets tech jargon they don't understand. Auto-fail triggers because tone is wrong.

## Q3: Why did you choose single prompt over chain?
**Answer:** Simpler to debug, lower latency, less chance of schema breaking between steps.

## Q4: How do you ensure strategy chips are different?
**Answer:** Three philosophies: past-focused (accountability), future-focused (solutions), process-focused (understanding).

## Q5: What's your fallback if API fails?
**Answer:** Hardcoded valid JSON scenarios for both ICPs that still meet schema requirements.

## Q6: How do rubric scores change by milestone?
**Answer:** M01 easier → higher scores (60-70). M07 harder → lower scores (20-40). Never all 50s.

## Q7: How do you handle missing fields in input?
**Answer:** Default values: episode_title="Workplace Challenge", milestone_code="M01", skill_target="communication".

## Q8: Show me what changes when you edit the prompt?
**Answer:** [Be ready to edit prompts.py and show different output]