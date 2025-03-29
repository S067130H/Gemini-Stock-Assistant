"""
This module contains the definition of the get_news_sentiment function and the bundle_tools function.
The get_news_sentiment function is used to retrieve the latest news sentiment for a list of stock tickers or topics.
The bundle_tools function is used to wrap the function declarations into a tool format for use with the GenAI API.
"""

from typing import Optional
from google.genai import types

get_news_sentiment = types.FunctionDeclaration(
    name="get_news_sentiment",
    description="Get the latest news sentiment for a list of stock tickers or topics.",
    parameters={
        "type": "object",
        "properties": {
            "tickers": {
                "type": "array",
                "items": {"type": "string"},
                "description": "A list of stock ticker symbols (e.g. AAPL, TSLA).",
            },
            "topics": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Optional topics to filter the news sentiment by.",
            },
        },
        "required": [],  # None are required — matches your AlphaVantageClient logic
    },
)


def bundle_tools(
    functions: Optional[list[types.FunctionDeclaration]],
) -> Optional[list[types.Tool]]:
    """
    Wraps function declarations into a tool format for use with the GenAI API.
    """
    return [types.Tool(function_declarations=functions)] if functions else None
