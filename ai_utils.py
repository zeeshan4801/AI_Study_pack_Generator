import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_ai(prompt):

    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role":"system","content":"You are an educational AI assistant."},
                    {"role":"user","content":prompt}
                ]
            )
            return response.choices[0].message.content

        except Exception as e:
            print(e)
            time.sleep(2)

    return "AI generation failed."
