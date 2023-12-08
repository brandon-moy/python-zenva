import openai


from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("CHATGPT_API_KEY")

# Pass the API key
openai.api_key = api_key

# Define prompt
message = { "role": "user", "content": "why is the sky blue?"}

messages = []
messages.append(message)

# Make an API call

# Print the response