# 📈 Gemini Stock Assistant
# 📈 Gemini Stock Assistant

Gemini Stock Assistant is an AI-powered CLI application that uses Google Gemini + Alpha Vantage to generate market insights based on real-time news sentiment.

Ask natural questions like:

> _"What’s the latest news sentiment for AAPL and MSFT?"_

The app:
- Uses **Gemini’s function calling** to detect that you want news sentiment
- Calls **Alpha Vantage’s `NEWS_SENTIMENT` API**
- **Summarizes** the result using Gemini
- Caches the results for fast reuse

---

## 🚀 Features
Gemini Stock Assistant is an AI-powered CLI application that uses Google Gemini + Alpha Vantage to generate market insights based on real-time news sentiment.

Ask natural questions like:

> _"What’s the latest news sentiment for AAPL and MSFT?"_

The app:
- Uses **Gemini’s function calling** to detect that you want news sentiment
- Calls **Alpha Vantage’s `NEWS_SENTIMENT` API**
- **Summarizes** the result using Gemini
- Caches the results for fast reuse

---

## 🚀 Features

- 🤖 **AI-Driven Insight** – Uses Gemini 2.0 to summarize and analyze news data
- 🔍 **Real-Time News Sentiment** – Pulls structured sentiment data from Alpha Vantage
- 🧠 **Function Calling** – Gemini auto-triggers a tool to get the data it needs
- ⚡ **Streaming Output** – Live token-by-token output for faster feedback
- 🗂️ **Caching** – API results are cached to avoid duplicate calls and improve speed

---

## 🧱 Architecture

| Component | Description |
|----------|-------------|
| `main.py` | CLI entry point — handles prompt input, function routing, summarization |
| `genai_api.py` | Gemini client with support for generation, streaming, and summarization |
| `alpha_vantage_api.py` | Fetches and caches Alpha Vantage news sentiment data |
| `tools.py` | Defines Gemini function tools like `get_news_sentiment()` |

---

## 🧪 Example Prompts

- `What’s the latest sentiment around Apple and Microsoft?`
- `Summarize the tech and AI sectors this week.`
- `What are people saying about Tesla and Nvidia?`

---

## 🛠️ Installation
- 🤖 **AI-Driven Insight** – Uses Gemini 2.0 to summarize and analyze news data
- 🔍 **Real-Time News Sentiment** – Pulls structured sentiment data from Alpha Vantage
- 🧠 **Function Calling** – Gemini auto-triggers a tool to get the data it needs
- ⚡ **Streaming Output** – Live token-by-token output for faster feedback
- 🗂️ **Caching** – API results are cached to avoid duplicate calls and improve speed

---

## 🧱 Architecture

| Component | Description |
|----------|-------------|
| `main.py` | CLI entry point — handles prompt input, function routing, summarization |
| `genai_api.py` | Gemini client with support for generation, streaming, and summarization |
| `alpha_vantage_api.py` | Fetches and caches Alpha Vantage news sentiment data |
| `tools.py` | Defines Gemini function tools like `get_news_sentiment()` |

---

## 🧪 Example Prompts

- `What’s the latest sentiment around Apple and Microsoft?`
- `Summarize the tech and AI sectors this week.`
- `What are people saying about Tesla and Nvidia?`

---

## 🛠️ Installation

1. Clone the project
```bash
git clone https://github.com/S067130H/Gemini-Stock-Assistant.git
cd gemini-stock-assistant
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```
2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Add a `.env` file with your keys:
```
GENAI_API_KEY=your_google_genai_key
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key
4. Add a `.env` file with your keys:
```
GENAI_API_KEY=your_google_genai_key
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key
```

---

## 🧠 How It Works (Behind the Scenes)

1. You enter a natural prompt.
2. Gemini tries to complete the response — and if needed, **calls a registered tool**.
3. The `get_news_sentiment` tool hits Alpha Vantage and returns structured news data.
4. Gemini **summarizes** this data using a financial analyst persona.
5. The result is **streamed token-by-token** to your console.

Cached results are stored in `/cache` using a hash of the tickers/topics.

---

## 📁 Example Cache Files

```
cache/
├── 0ee7055184601ceace9296c8ffe52695.json  # Cached result for AAPL + MSFT
├── 813b48dbce92baecd34d4fddd07e27ff.json  # Cached result for tech + AI
```

---

## 💡 Future Ideas

- Visualize sentiment data with charts
- Export summaries to markdown or JSON
- Add more tools (price history, portfolio generation)

---

## 📜 License

MIT [License](LICENSE)
---

## 🧠 How It Works (Behind the Scenes)

1. You enter a natural prompt.
2. Gemini tries to complete the response — and if needed, **calls a registered tool**.
3. The `get_news_sentiment` tool hits Alpha Vantage and returns structured news data.
4. Gemini **summarizes** this data using a financial analyst persona.
5. The result is **streamed token-by-token** to your console.

Cached results are stored in `/cache` using a hash of the tickers/topics.

---

## 📁 Example Cache Files

```
cache/
├── 0ee7055184601ceace9296c8ffe52695.json  # Cached result for AAPL + MSFT
├── 813b48dbce92baecd34d4fddd07e27ff.json  # Cached result for tech + AI
```

---

## 💡 Future Ideas

- Visualize sentiment data with charts
- Export summaries to markdown or JSON
- Add more tools (price history, portfolio generation)

---

## 📜 License

MIT [License](LICENSE)