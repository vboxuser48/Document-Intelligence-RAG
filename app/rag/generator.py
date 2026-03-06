from google import genai
import os

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_answer(context_chunks, question):

    context = "\n".join(context_chunks)

    prompt = f"""
Answer the question using the context.

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    return response.text