import os
import time
from groq import Groq
from dotenv import load_dotenv


load_dotenv()


# Groq API Connection
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def call_ai(prompt):

    for attempt in range(3):

        try:

            response = client.chat.completions.create(

                # GPT OSS 20B model
                model="openai/gpt-oss-20b",

                messages=[

                    {
                        "role": "system",
                        "content": """
                        You are an expert AI education assistant.
                        Create accurate, personalized study materials.
                        """
                    },

                    {
                        "role": "user",
                        "content": prompt
                    }

                ],

                temperature=0.7,

                max_tokens=4000

            )


            return response.choices[0].message.content


        except Exception as e:

            print(
                f"Attempt {attempt+1} failed: {e}"
            )

            time.sleep(2)


    return "AI generation failed."
