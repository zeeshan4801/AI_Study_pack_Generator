PLANNING_PROMPT = """
You are a study planning expert.
Create a personalized learning roadmap.

Student information:
{data}

Include objectives, schedule, concepts and strategy.
"""

CONTENT_PROMPT = """
You are an expert teacher.

Student:
{data}

Study plan:
{plan}

Create explanations, examples, key points and memory techniques.
"""

ASSESSMENT_PROMPT = """
Create an assessment from this content:

{content}

Generate MCQs with answers, short questions and long questions.
"""

REVIEW_PROMPT = """
Review this study pack:

{pack}

Check accuracy, completeness and difficulty level.
Give improvement feedback.
"""

REFINEMENT_PROMPT = """
You are the final editor.

Study pack:
{pack}

Review:
{review}

Create the final polished personalized study pack.
"""
