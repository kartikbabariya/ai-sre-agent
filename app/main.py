from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

client = OpenAI()


class IncidentAnalysis(BaseModel):
    incident_type: str
    severity: str
    evidence: list[str]
    possible_causes: list[str]
    missing_information: list[str]
    next_actions: list[str]


response = client.responses.parse(
    model="gpt-5.6-luna",
    input="""
    You are an AI SRE assistant.

    A production API is returning HTTP 500 errors.

    Analyse the incident.

    Do not assume the root cause without evidence.
    Clearly separate evidence from possible causes.
    Tell us what information is still missing.
    """,
    text_format=IncidentAnalysis,
)

analysis = response.output_parsed

print("Incident type:", analysis.incident_type)
print("Severity:", analysis.severity)

print("\nEvidence:")
for item in analysis.evidence:
    print("-", item)

print("\nPossible causes:")
for item in analysis.possible_causes:
    print("-", item)

print("\nMissing information:")
for item in analysis.missing_information:
    print("-", item)

print("\nNext actions:")
for item in analysis.next_actions:
    print("-", item)