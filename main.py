import os
from dotenv import load_dotenv
from openai import OpenAI

# load environment variables
load_dotenv()

api_key = os.environ.get("OPENROUTER_API_KEY")
# raise a RuntimeError if the key is not found
if api_key is None :
    raise RuntimeError("api key not found !")

# create a client
# we point the client's base url to openrouter instead of openai
client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = api_key,
)

# model = "openrouter/free"
model = "openai/gpt-oss-20b:free"
# a hard-coded role and question for testing
# messages are saved in a dictionary / object with the role and content keys
messages = [
    {
        "role": "user",
        "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    }
]

# this generates a response from the LLMs we will use
# takes two parameters, model and messages 
client.chat.completions.create(messages, model)

print(response.choices[0].message.content)
# def main():
#     print("Hello from ai-agent!")

if __name__ == "__main__":
    # main()
    pass