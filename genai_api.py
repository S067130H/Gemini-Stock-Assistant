"""
This module provides a client for interacting with the Google GenAI API.
It allows for generating content and streaming responses using the specified model and instructions.
"""

import os
import json
from typing import Optional
from google import genai
from google.genai import types
from tools import bundle_tools


class GenAIClient:
    """
    A client for interacting with the Google GenAI API.
    """

    def __init__(
        self,
        api_key=None,
        model: str = "gemini-2.0-flash",
        instructions: str = "You are a financial advisor.",
    ):
        self.api_key = api_key or os.getenv("GENAI_API_KEY")
        self.model = model
        self.instructions = instructions

        if not self.api_key:
            raise ValueError("API key is required.")

        self.client = genai.Client(api_key=self.api_key)

    def _build_config(self, tools: Optional[list[types.FunctionDeclaration]] = None):
        """
        Build the configuration for the GenAI API request.
        """
        return types.GenerateContentConfig(
            system_instruction=self.instructions,
            tools=bundle_tools(tools),  # Ensure tools are wrapped correctly
        )

    def get_response(
        self,
        contents: str,
        tools: Optional[list[types.FunctionDeclaration]] = None,
    ):
        """
        Generate a response using the GenAI API.
        """
        response = self.client.models.generate_content(
            model=self.model,
            config=self._build_config(tools),
            contents=contents,
        )

        return response

    def stream_response(
        self,
        contents: str,
        tools: Optional[list[types.FunctionDeclaration]] = None,
    ):
        """
        Stream a response using the GenAI API.
        """
        response = self.client.models.generate_content_stream(
            model=self.model,
            config=self._build_config(tools),
            contents=contents,
        )

        return response

    def summarize_sentiment(
        self,
        sentiment_data: dict,
        max_items: int = 3,
        tools: Optional[list[types.FunctionDeclaration]] = None,
    ):
        """
        Summarize news sentiment data using the GenAI API.
        """
        articles = sentiment_data.get("feed", [])[:max_items]
        prompt = f"""
        You are a market analyst. Analyze and summarize the following news sentiment data.

        Focus on:
        - Overall market mood
        - Bullish or bearish trends
        - Notable companies mentioned
        - Any sector-specific patterns

        Return a concise plain-English summary.

        News data:
        {json.dumps(articles, indent=2)}
        """

        return self.get_response(contents=prompt, tools=tools)
