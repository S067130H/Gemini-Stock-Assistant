"""
This module provides a client for the Alpha Vantage API, specifically for the NEWS_SENTIMENT function.
It allows for retrieving news sentiment based on provided tickers or topics.
"""

import os
import json
import time
import hashlib
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

    def cache_response(
        self, tickers: list[str], topics: list[str], response: dict, cache_dir: str
    ) -> None:
        """
        Cache the response to a file in the specified directory.
        """
        os.makedirs(cache_dir, exist_ok=True)
        cache_key = self._generate_cache_key(tickers, topics)
        cache_path = os.path.join(cache_dir, f"{cache_key}.json")

        with open(cache_path, "w") as f:
            json.dump(response, f)

    def _generate_cache_key(self, tickers: list[str], topics: list[str]) -> str:
        """
        Generate a unique cache key based on the tickers and topics.
        """
        data = json.dumps(
            {"tickers": sorted(tickers or []), "topics": sorted(topics or [])},
            sort_keys=True,
        )
        return hashlib.md5(data.encode("utf-8")).hexdigest()

    def load_from_cache(
        self, tickers: list[str], topics: list[str], cache_dir: str, max_age: int = 3600
    ) -> dict | None:
        """
        Load the cached response from a file in the specified directory.
        """
        cache_key = self._generate_cache_key(tickers, topics)
        cache_path = os.path.join(cache_dir, f"{cache_key}.json")

        if os.path.exists(cache_path):
            age = time.time() - os.path.getmtime(cache_path)
            if age < max_age:
                with open(cache_path, "r") as f:
                    return json.load(f)
            else:
                os.remove(cache_path)
        return None
