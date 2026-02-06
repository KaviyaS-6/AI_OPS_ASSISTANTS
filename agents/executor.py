from tools.weather_tool import get_weather
from tools.github_tool import create_repo

def executor_agent(plan):

    results = []

    for step in plan["steps"]:
        tool = step.get("tool")
        tool_input = step.get("input")  # Get input from planner step

        if tool == "weather":
            results.append(get_weather(tool_input))

        elif tool == "github":
            # Extract repo name from planner input
            # Example input: "create repository ai-test-repo"
            repo_name = tool_input.split()[-1]
            result = create_repo(repo_name)
            results.append(result)

    return results
