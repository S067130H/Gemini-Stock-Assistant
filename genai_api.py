import os
from typing import Optional
from google import genai
from google.genai import types
from tools import bundle_tools


class GenAIClient:
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
        return types.GenerateContentConfig(
            system_instruction=self.instructions,
            tools=bundle_tools(tools),  # Ensure tools are wrapped correctly
        )

    def get_response(
        self,
        contents: str,
        tools: Optional[list[types.FunctionDeclaration]] = None,
    ):
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
        response = self.client.models.generate_content_stream(
            model=self.model,
            config=self._build_config(tools),
            contents=contents,
        )

        return response
