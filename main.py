'''
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API KEY:", api_key)



from google.adk.runners import Runner
from agent import travel_agent

runner = Runner(agent=travel_agent)

user_request = "Plan a 3-day trip from Hyderabad to Delhi"

response = runner.run(user_request)
#response = travel_agent.run(input = user_request)
#response = travel_agent.run({"input" == user_request})
print(response)
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from agent import travel_agent

# Create session service
session_service = InMemorySessionService()

# Create runner
runner = Runner(
    agent=travel_agent,
    app_name="Travel_Agent",
    session_service=session_service
)

query = "Plan a 3-day trip from Hyderabad to Delhi"

response = runner.run(user_input=query)

print(response)
'''

import asyncio
from google.adk.agents import Agent
from google.adk.agents import LlmAgent
from google.adk.runners import InMemoryRunner

from google.genai.types import Content, Part
from dotenv import load_dotenv

from agent import travel_agent as agent

load_dotenv()

'''
agent = LlmAgent(
    model = "gemini-2.5-flash",
    name = "FlightAgent",
    description = """
    Your departure is {departure}.
    Tell me the optimal route between flights
    """,
    tools = [PreloadMemoryTool()]

)

runner = InMemoryRunner(agent=agent, app_name="agents")

async def run_dialogue():
    # first session id 
    session_id = "session_1"

    # create a session service 
    await runner.session_service.create_session(
        app_name = runner.app_name,
        user_id = "user1",
        session_id = session_id,
    )
    print(f"user: I am travelling from Hyderabad to Delhi, show me flights")
    content = Content(role="user", parts=[Part(text="I am travelling from Hyderabad to Delhi, show me flights")])

    async for event in runner.run_async(user_id="user1", session_id = session_id, new_message=content):
        # check if event has content and it is from the agent (not user)
        if event.content and event.content.parts and event.author != "user":
            for part in event.content.parts:
                if part.text:
                    print(f"Agent: {part.text}")

    # after conversation, save to memory 
    session = await runner.session_service.get_session(
        app_name = runner.app_name,
        user_id = "user1",
        session_id = session_id
    )

    await runner.memory_service.add_session_to_memory(session)

    print("\n")
    print(f"user: Where am I travelling?")
    content = Content(role="user", parts=[Part(text="Where i am travelling?")])

    async for event in runner.run_async(user_id="user1", session_id=session_id, new_message=content):
        # check if event has content and it is from the agent (not user)
        if event.content and event.content.parts and event.author != "user":
            for part in event.content.parts:
                if part.text:
                    print(f"Agent: {part.text}")


asyncio.run(run_dialogue())
'''
import asyncio
from agent import travel_agent as agent
from google.adk.runners import InMemoryRunner
from google.adk.tools.preload_memory_tool import PreloadMemoryTool
from google.genai.types import Content, Part


runner = InMemoryRunner(agent=agent, app_name="agents")


async def chat():
    session_id = "chat_session"

    await runner.session_service.create_session(
        app_name=runner.app_name,
        user_id="user1",
        session_id=session_id,
    )

    print("🤖 Travel Agent Ready! (type 'exit' to quit)\n") 

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        content = Content(role="user", parts=[Part(text=user_input)])

        async for event in runner.run_async(
            user_id="user1",
            session_id=session_id,
            new_message=content
        ):
            if event.content and event.content.parts and event.author != "user":
                for part in event.content.parts:
                    if part.text:
                        print(f"Agent: {part.text}")


asyncio.run(chat())