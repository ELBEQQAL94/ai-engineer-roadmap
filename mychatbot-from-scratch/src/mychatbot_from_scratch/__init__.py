from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

while True:
    query = input("User: ")
    if query == "GO":
        break
    loading = "Loading..."
    print(loading, end="", flush=True)
    response = client.responses.create(
        model="gpt-4o-mini",
        input=query
    )
    print("\r" + " " * len(loading) + "\r", end="")
    print(f"AI: {response.output_text}")
