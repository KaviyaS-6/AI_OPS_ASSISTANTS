from llm.llm_client import call_llm


def verifier_agent(results):

    prompt = f"""
Verify if this output is complete and correct.

Results:
{results}

Return improved structured summary.
"""

    return call_llm(prompt)
