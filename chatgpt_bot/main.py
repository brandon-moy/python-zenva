from openai import OpenAI


from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("CHATGPT_API_KEY")

# Pass the API key
client = OpenAI(api_key=api_key)

# Define prompt
message = { "role": "user", "content": "why is the sky blue?"}

messages = []
messages.append(message)

# Make an API call
chat_completion = client.chat.completions.create(messages=messages, model="gpt-3.5-turbo")

# Print the response
print(chat_completion)