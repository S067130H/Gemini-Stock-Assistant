# Gemini Stock Assistant

Gemini Stock Assistant is a Python-based application that leverages Google's Gemini API to provide real-time financial insights. It supports advanced tool-calling capabilities to trigger custom functions, such as retrieving news sentiment data via the Alpha Vantage API. The project is modular, scalable, and designed to streamline financial analysis.

## Features

- **Google Gemini API Integration**: Provides financial insights and supports both streaming and non-streaming responses.
- **Tool Calling**: Uses `FunctionDeclaration` to trigger custom tools like `get_news_sentiment`.
- **Real-Time News Sentiment**: Retrieves sentiment data for stock tickers or topics using the Alpha Vantage API.
- **Modular Design**: Includes `GenAIClient` for Gemini API interactions and `AlphaVantageClient` for Alpha Vantage API calls.
- **Dynamic Function Routing**: Routes function calls from Gemini to actual implementations and processes JSON results.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/S067130H/gemini-stock-assistant.git
    cd gemini-stock-assistant
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Set up environment variables (see below).

## Environment Variable Setup

Create a `.env` file in the project root with the following keys:

```env
GENAI_API_KEY=your_google_genai_api_key
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
```

Replace `your_google_genai_api_key` and `your_alpha_vantage_api_key` with your actual API keys.

## Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. Enter a prompt when prompted. For example:
    ```
    Enter a prompt for news sentiment analysis: Summarize tech market sentiment for AAPL and MSFT
    ```

3. The application will:
    - Use the Gemini API to process the prompt.
    - Trigger the `get_news_sentiment` tool if required.
    - Fetch real-time sentiment data from the Alpha Vantage API.
    - Summarize the results and display them.

### Example Workflow

**Input Prompt**:  
`Summarize tech market sentiment for AAPL and MSFT`

**Function Call**:  
`get_news_sentiment` is triggered with `tickers=["AAPL", "MSFT"]`.

**Response**:  
```
News Sentiment: {"AAPL": "Positive", "MSFT": "Neutral"}
```

## Future Features

- **Enhanced Tooling**: Add more tools for financial analysis, such as stock price predictions or portfolio optimization.
- **Web Interface**: Build a web-based dashboard for easier interaction.
- **Data Visualization**: Integrate charts and graphs for better insights.
- **Multi-Language Support**: Expand support for non-English financial news.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
