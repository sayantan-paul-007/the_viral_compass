# #This is the base code from Kaggle about root agent using Sequential Agent to connect all the orchestrator agents.
# from google.adk.agents import SequentialAgent, InMemoryRunner
# from backend.src.agents.content_analyst_agent import content_analyst_agent  
# from backend.src.agents.trend_research_agent import trend_research_agent
# from backend.src.agents.creative_strategist_agent import creative_strategist_agent
# from backend.src.agents.final_report_agent import final_report_agent
# root_agent = SequentialAgent(
#     name="root_agent",
#     description="This agent is responsible for connecting the orchestrator agents",
#     sub_agents=[content_analyst_agent, trend_research_agent,creative_strategist_agent,final_report_agent ],
# )
# runner = InMemoryRunner(agent=root_agent)
from google.adk.agents import SequentialAgent
from google.adk.runners import InMemoryRunner

from agents.content_analyst_agent import content_analyst_agent  
from agents.trend_research_agent import trend_research_agent
from agents.creative_strategist_agent import creative_strategist_agent
from agents.final_report_agent import final_report_agent


def build_runner() -> InMemoryRunner:
    """
    Creates and returns the root agent runner.
    """
    root_agent = SequentialAgent(
        name="root_agent",
        description="This agent is responsible for connecting the orchestrator agents",
        sub_agents=[
            content_analyst_agent,
            trend_research_agent,
            creative_strategist_agent,
            final_report_agent,
        ],
    )

    runner = InMemoryRunner(agent=root_agent)
    print("✅ Root Agent runner created")

    return runner
