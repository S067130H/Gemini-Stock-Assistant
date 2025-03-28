from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
    )

    print(response.text)

if __name__ == "__main__":
    main()