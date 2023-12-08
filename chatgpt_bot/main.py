import openai


from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("CHATGPT_API_KEY")

# Pass the API key
openai.api_key = api_key

# Define prompt


# Make an API call


# Print the response