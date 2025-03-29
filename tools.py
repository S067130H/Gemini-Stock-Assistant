from typing import Optional
from google.genai import types

get_news_sentiment = types.FunctionDeclaration(
    name="get_news_sentiment",
    description="Get the latest news sentiment for a list of tickers or topics.",
    parameters=types.FunctionParameters(
        properties={
            "tickers": types.FunctionParameter(
                name="tickers",
                description="List of stock tickers to get news sentiment for.",
                type=types.ParameterType.ARRAY,
                items=types.FunctionParameter(
                    type=types.ParameterType.STRING,
                    description="A stock ticker symbol.",
                ),
            ),
            "topics": types.FunctionParameter(
                name="topics",
                description="List of topics to get news sentiment for.",
                type=types.ParameterType.ARRAY,
                items=types.FunctionParameter(
                    type=types.ParameterType.STRING,
                    description="A topic of interest.",
                ),
            ),
        },
        required=[],  # Make both optional to match AlphaVantageClient logic
    ),
)


def bundle_tools(
    functions: Optional[list[types.FunctionDeclaration]],
) -> Optional[list[types.Tool]]:
    return [types.Tool(function_declarations=functions)] if functions else None
