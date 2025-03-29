"""
This module contains the definition of the get_news_sentiment function and the bundle_tools function.
The get_news_sentiment function is used to retrieve the latest news sentiment for a list of stock tickers or topics.
The bundle_tools function is used to wrap the function declarations into a tool format for use with the GenAI API.
"""

from typing import Optional
from google.genai import types

get_news_sentiment = types.FunctionDeclaration(
    name="get_news_sentiment",
    description="Get the latest news sentiment for a list of tickers or topics.",
    parameters={
        "properties": {
            "tickers": {
                "description": "List of stock tickers to get news sentiment for.",
                "type": "array",
                "items": {
                    "type": "string",
                    "description": "A stock ticker symbol.",
                },
            },
            "topics": {
                "description": "List of topics to get news sentiment for.",
                "type": "array",
                "items": {
                    "type": "string",
                    "description": "A topic of interest.",
                },
            },
        },
        "required": [],  # Make both optional to match AlphaVantageClient logic
    },
)


def bundle_tools(
    functions: Optional[list[types.FunctionDeclaration]],
) -> Optional[list[types.Tool]]:
    """
    Wraps function declarations into a tool format for use with the GenAI API.
    """
    return [types.Tool(function_declarations=functions)] if functions else None
