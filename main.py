"""
This script is a simple command-line application that uses the Google GenAI API to analyze news sentiment based on user input.
It initializes the GenAI and Alpha Vantage clients, accepts a user prompt, and generates a summary of the latest news articles.
If a function call is detected in the response, it retrieves the news sentiment using the Alpha Vantage API and prints the result.
"""

import os
import time
from dotenv import load_dotenv
from genai_api import GenAIClient
from alpha_vantage_api import AlphaVantageClient
from tools import get_news_sentiment

load_dotenv()


cache_dir = os.path.join(os.path.dirname(__file__), "cache")


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
            if chunk.candidates[0].content.parts[0].function_call:
                function_call = chunk.candidates[0].content.parts[0].function_call
                if function_call.name == "get_news_sentiment":
                    # Extract arguments from the function call
                    args = function_call.args
                    tickers = args.get("tickers", [])
                    topics = args.get("topics", [])

                    # Attempt to load data from cache
                    cached_data = avc.load_from_cache(tickers, topics, cache_dir)
                    if cached_data:
                        print("Using cached data.")
                        # Use the cached data for sentiment analysis
                        response = gemini.summarize_sentiment(
                            sentiment_data=cached_data,
                            tools=[get_news_sentiment],
                        )

                        for text in gemini.stream_text_from_response(response):
                            for char in text:
                                print(char, end="")
                                time.sleep(
                                    0.01
                                )  # Add a small delay for better readability
                    else:
                        print(f"Fetching data from API...", end="")
                        start_time = time.time()

                        # Fetch data from the API
                        sentiment = avc.get_news_sentiment(
                            tickers=tickers, topics=topics
                        )

                        elapsed_time = time.time() - start_time
                        print(f" Done! (Time elapsed: {elapsed_time:.2f} seconds)")

                        # Cache the response
                        avc.cache_response(tickers, topics, sentiment, cache_dir)
                        print("Data cached.")

                        response = gemini.summarize_sentiment(
                            sentiment_data=sentiment,
                            tools=[get_news_sentiment],
                        )

                        for text in gemini.stream_text_from_response(response):
                            for char in text:
                                print(char, end="")
                                time.sleep(0.01)
            else:
                print(chunk.text, end="")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
