"""
This script is a simple command-line application that uses the Google GenAI API to analyze news sentiment based on user input.
It initializes the GenAI and Alpha Vantage clients, accepts a user prompt, and generates a summary of the latest news articles.
If a function call is detected in the response, it retrieves the news sentiment using the Alpha Vantage API and prints the result.
"""

import os
from dotenv import load_dotenv
from genai_api import GenAIClient
from alpha_vantage_api import AlphaVantageClient
from tools import get_news_sentiment

load_dotenv()


def main():
    """
    Main function to run the sentiment analysis.
    """
    try:
        # Verify that the GENAI API key is set
        if not os.getenv("GENAI_API_KEY"):
            raise ValueError("GENAI_API_KEY is required.")

        # Initialize the clients
        gemini = GenAIClient()
        avc = AlphaVantageClient()

        # Accept a user prompt for news sentiment analysis
        user_prompt = input("Enter a prompt for news sentiment analysis: ")

        # Generate a summary of the latest news articles
        response = gemini.stream_response(
            contents=user_prompt,
            tools=[get_news_sentiment],
        )

        # Process the response and handle function calls
        for chunk in response:
            if chunk.function_call:
                if chunk.function_call.name == "get_news_sentiment":
                    # Extract arguments and call AlphaVantageClient
                    args = chunk.function_call.arguments
                    tickers = args.get("tickers", [])
                    topics = args.get("topics", [])
                    sentiment = avc.get_news_sentiment(tickers=tickers, topics=topics)
                    print(f"News Sentiment: {sentiment}")
            else:
                print(chunk.text, end="")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
