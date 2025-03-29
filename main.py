import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from alpha_vantage_api import AlphaVantageClient

load_dotenv()


def main():
    try:
        # Verify that the GENAI API key is set
        if not os.getenv("GENAI_API_KEY"):
            raise ValueError("GENAI_API_KEY is required.")

        # Initialize the clients
        avc = AlphaVantageClient()
        client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

        response = client.models.generate_content_stream(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                # System instruction to set the context for the model.
                system_instruction="You are a financial advisor.",
            ),
            # Prompt for the model to generate content for.
            contents="Explain how to create a portfolio.",
        )

        # Print the response as it is received in chunks.
        for chunk in response:
            print(chunk.text, end="")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
