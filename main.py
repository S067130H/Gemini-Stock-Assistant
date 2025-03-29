import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from genai_api import GenAIClient
from alpha_vantage_api import AlphaVantageClient

load_dotenv()


def main():
    try:
        # Verify that the GENAI API key is set
        if not os.getenv("GENAI_API_KEY"):
            raise ValueError("GENAI_API_KEY is required.")

        # Initialize the clients
        gemini = GenAIClient()
        avc = AlphaVantageClient()

        response = gemini.stream_response(
            contents="Generate a summary of the latest news articles.",
            # tools=[avc.get_news_sentiment],
        )

        # Print the response as it is received in chunks.
        for chunk in response:
            print(chunk.text, end="")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
