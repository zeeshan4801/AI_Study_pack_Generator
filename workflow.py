from prompts import *
from ai_utils import call_ai

def planning_agent(data):
    return call_ai(PLANNING_PROMPT.format(data=data))

def content_agent(plan, data):
    return call_ai(CONTENT_PROMPT.format(plan=plan, data=data))

def assessment_agent(content):
    return call_ai(ASSESSMENT_PROMPT.format(content=content))

def review_agent(pack):
    return call_ai(REVIEW_PROMPT.format(pack=pack))

def refinement_agent(pack, review):
    return call_ai(REFINEMENT_PROMPT.format(pack=pack, review=review))

def generate_study_pack(student):

    context = {}

    context["plan"] = planning_agent(student)
    context["content"] = content_agent(context["plan"], student)
    context["assessment"] = assessment_agent(context["content"])

    draft = f"""
PLAN:
{context['plan']}

CONTENT:
{context['content']}

ASSESSMENT:
{context['assessment']}
"""

    context["review"] = review_agent(draft)
    context["final"] = refinement_agent(draft, context["review"])

    return context
