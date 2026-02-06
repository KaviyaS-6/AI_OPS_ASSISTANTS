from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.verifier import verifier_agent


def run_assistant(query):

    plan = planner_agent(query)
    print("PLAN:", plan)

    results = executor_agent(plan)
    print("RAW RESULTS:", results)

    final_output = verifier_agent(results)

    return final_output


if __name__ == "__main__":

    user_query = input("Enter your task: ")
    output = run_assistant(user_query)

    print("\nFINAL OUTPUT:")
    print(output)
