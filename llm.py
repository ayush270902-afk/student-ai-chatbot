
from groq import Groq
import os

# Initialize Groq client using Streamlit Secrets
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate(prompt: str) -> str:
    """
    Generate response using Groq-hosted LLM
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful student assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=512
    )

    return response.choices[0].message.content
