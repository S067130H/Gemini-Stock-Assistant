"""
This module provides a client for the Alpha Vantage API, specifically for the NEWS_SENTIMENT function.
It allows for retrieving news sentiment based on provided tickers or topics.
"""

import os
import requests


class AlphaVantageClient:
    """
    A client for interacting with the Alpha Vantage API.
    """

    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("ALPHA_VANTAGE_API_KEY")

        if not self.api_key:
            raise ValueError("API key is required.")

    def get_news_sentiment(
        self, tickers: list[str] = None, topics: list[str] = None
    ) -> dict:
        """
        Retrieve news sentiment for the specified tickers or topics.
        """
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "NEWS_SENTIMENT",
            "apikey": self.api_key,
        }

        if not tickers and not topics:
            raise ValueError("At least one of 'tickers' or 'topics' must be provided.")

        if tickers:
            params["tickers"] = ",".join([ticker.upper() for ticker in tickers])
        if topics:
            params["topics"] = ",".join([topic.lower() for topic in topics])

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
