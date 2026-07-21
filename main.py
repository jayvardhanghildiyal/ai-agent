import os, json
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from config import system_prompt
from functions.call_function import available_functions
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

# we create an argument parser that takes in a user-request
parser = argparse.ArgumentParser(description="talk to a LLM !")
parser.add_argument("user_prompt", type=str, help="the argument is a question asked to the LLM")
parser.add_argument("--verbose", action = "store_true", help = "allows the user to view verbose output")
args = parser.parse_args()

# message list to hold conversations
# the system prompt goes first to define the behaviour and rules set on the LLM
messages = [
    {"role" : "system", "content" : system_prompt},
    {"role": "user", "content": args.user_prompt}
]

# this generates a response from the LLMs we will use
# takes two parameters, model and messages 
# much later, we have now added a third parameter
# it provides a list of tools available to the LLM
response = client.chat.completions.create(
    model = "openrouter/free", 
    # messages are saved in a dictionary / object with the role and content keys
    messages = messages,
    tools = available_functions
)

# if the usage object is empty
if response.usage is None :
    raise RuntimeError("Likely failed API request")

# if verbose mode is on
if args.verbose :
    print(f"User prompt: {args.user_prompt}")
    # printing and tracking the number of tokens used 
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")

# addressing any tools that the LLM wants to call
# printing them for now
# print(response)
message = response.choices[0].message

for tool_call in message.tool_calls or []:
    func_args = json.loads(tool_call.function.arguments or "{}")
    print(f"Function call needed : {tool_call.function.name}({func_args})")

# print the response afterwards
print("\nResponse: \n")
print(response.choices[0].message.content)

# def main():
#     print("Hello from ai-agent!")

if __name__ == "__main__":
    # main()
    pass