from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5.6-luna",
    input="""
You are an AI SRE assistant.

A production API is returning HTTP 500 errors.

Your task is to investigate the incident.

First explain:
1. What information you would collect.
2. Which logs you would inspect.
3. Which infrastructure information you would check.
4. What possible causes you would investigate.

Do not assume the root cause without evidence.
"""
)

print(response.output_text)
