import os
import time
from groq import Groq
import streamlit as st


# Get API key from Streamlit secrets or environment

try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    api_key = os.getenv("GROQ_API_KEY")


client = Groq(
    api_key=api_key
)



def call_ai(prompt):

    for attempt in range(3):

        try:

            response = client.chat.completions.create(

                model="openai/gpt-oss-20b",

                messages=[

                    {
                        "role": "system",
                        "content":
                        "You are an expert AI education assistant."
                    },

                    {
                        "role": "user",
                        "content": prompt
                    }

                ],

                temperature=0.7

            )


            if response.choices:

                return response.choices[0].message.content


        except Exception as e:

            print("ERROR:", e)

            if attempt == 2:
                return f"AI Error: {str(e)}"

            time.sleep(2)


    return "AI generation failed"
