import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_plan(destination, days, budget, interests):

    prompt = f"""
    Create a detailed travel plan.

    Destination: {destination}
    Number of Days: {days}
    Budget: {budget}
    Interests: {interests}

    Include:
    1. Day-wise itinerary
    2. Hotel suggestions
    3. Food recommendations
    4. Packing list
    5. Estimated cost
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content