from dotenv import load_dotenv
from langchain.messages import HumanMessage, SystemMessage
from langchain.agents import create_agent

load_dotenv()

def sum(a,b):
    """ Add two numbers """
    return a + b

def sub(a,b):
    """ Sub two numbers """
    return a - b

def div(a,b):
    """ Devide two numbers """
    return a / b

def mult(a,b):
    """ Mutliply two numbers """
    return a * b

agent = create_agent(
    model="gpt-4o-mini",
    tools=[sum,mult,sub,div],
    system_prompt=SystemMessage(content="Act as assistant")
)

while True:
    query = input("User: ")
    if query == "GO":
        break

    result = agent.invoke(
        {
            "messages": HumanMessage(content=query)
        }
    )
    print(f"AI: {result["messages"][-1].content_blocks[0]['text']}")