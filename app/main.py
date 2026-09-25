from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5.6-luna",
    input="Explain what a production incident is in one simple paragraph."
)

print("Response from the model:")
print(response.output_text)