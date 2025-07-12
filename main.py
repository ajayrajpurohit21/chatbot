import os
from dotenv import load_dotenv

from google import genai
from google.genai import types

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

prompt = input("Ask Gemini: ")


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
)

print("Gemini:", response.text.strip())
