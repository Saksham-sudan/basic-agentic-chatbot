from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")

model = ChatOpenAI(
    model = "openai/gpt-4.1",
    temperature =0,
    api_key=github_token,
    base_url="https://models.github.ai/inference"
)
tools =[]
agent = create_react_agent(model, tools)

while True:
    user_input = input("\nYou: ").strip()

    print("\nAssistent: ", end="")
    for chunk in agent.stream(
        {"messages": [HumanMessage(content=user_input)]}
    ):
        if "agent" in chunk and "messages" in chunk["agent"]:
            for message in chunk["agent"]["messages"]:
                print(message.content, end="")