from pathlib import Path

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from .tools import get_weather, get_current_time, destination_research_agent, itinerary_builder_agent, travel_optimizer_agent

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

AGENT_MODEL = "openai/gpt-4o-mini"
# AGENT_MODEL = "ollama/gemma3"
# AGENT_MODEL = "gemini-2.0-flash"



root_agent = Agent(
    name="travel_planner_agent",
    model=LiteLlm(model=AGENT_MODEL), # no need for sequential 
    description="An agent that helps users plan their travel itineraries, including flights, accommodations, and activities.",
    # instruction="You are a travel planner agent. You will assist users in planning their travel itineraries by providing recommendations for flights, accommodations, and activities based on their preferences and requirements. You can check weather conditions and best times to visit destinations to provide informed travel advice.",
    # tools=[get_weather, get_current_time]
     sub_agents=[
        destination_research_agent,
        itinerary_builder_agent,
        travel_optimizer_agent,
    ]
)