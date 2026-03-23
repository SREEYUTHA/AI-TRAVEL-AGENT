from google.adk.agents import Agent
#from tools import search_flights, search_hotels, generate_itinerary
from google.adk.agents import LlmAgent
from google.adk.tools.preload_memory_tool import PreloadMemoryTool
from tools.map_tool import get_route_info
from tools.flights_tool import get_flights
from tools.places_tool import get_places

'''
travel_agent = Agent(
    name = "TravelPlannerAgent",
    description = "Helps users plan trips including flights, hotels, and itineraries",
    tools=[search_flights, search_hotels, generate_itinerary],
)
'''
travel_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="TravelAgent",
    description="""
You are a smart travel assistant.

Your job:
- Extract source and destination from user input
- DO NOT immediately call tools

Conversation flow:
1. When user mentions travel (e.g., "Hyderabad to Delhi"):
   → Ask what they want:
     - Flights
     - Route
     - Places to visit

2. Only call tools AFTER user chooses:
   - Flights → use get_flights
   - Route → use get_route_info
   - Places → use get_places

3. Keep responses friendly and interactive

4. Maintain context of previous cities

Example:
User: I am travelling from Hyderabad to Delhi
Agent: What would you like to know?
        1. Flights ✈️
        2. Route 🗺️
        3. Places 📍
""",
    tools=[PreloadMemoryTool(), get_route_info, get_flights, get_places]
)

