import json
import re
from llm.llm_client import call_llm


def extract_json(text):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return json.loads(match.group())
    return {"steps": []}


def planner_agent(user_query):

    prompt = f"""
You are a planning agent.

Return ONLY valid JSON.

JSON format:
{{
    "steps": [
        {{"tool": "weather", "input": "city"}},
        {{"tool": "github", "input": "topic"}}
    ]
}}

User Query: {user_query}
"""

    result = call_llm(prompt)
    return extract_json(result)
