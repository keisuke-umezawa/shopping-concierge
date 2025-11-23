# Shopping Concierge

A shopping concierge agent built with Google's Agent Development Kit (ADK) to help users find and recommend products based on their preferences and needs.

## Overview

This agent provides personalized shopping assistance by understanding user preferences, searching for relevant products, and making tailored recommendations. It can help with product discovery, comparisons, and purchasing decisions.

### Agent Details

The shopping-concierge agent has the following capabilities:

- Understands user shopping preferences and requirements
- Searches for relevant products across different categories
- Provides personalized product recommendations
- Compares product features and prices
- Assists with purchasing decisions

| Feature | Description |
|---------|-------------|
| **Interaction Type** | Conversational |
| **Complexity** | Easy to Intermediate |
| **Agent Type** | Single Agent |
| **Vertical** | E-Commerce / Retail |

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) for dependency management
- Google Cloud Project with Vertex AI API enabled (recommended)
- OR a Gemini API key

### Installing uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/keisuke-umezawa/shopping-concierge.git
cd shopping-concierge
```

### 2. Install Dependencies

```bash
uv sync
```

### 3. Configure Environment Variables

Copy the `.env.example` file to `.env` and fill in your configuration:

```bash
cp .env.example .env
```

Edit the `.env` file with your settings:

```bash
# Required: Your Google Cloud Project ID
PROJECT_ID=your-project-id

# Required: Your Google Cloud Project Location
LOCATION=us-central1

# Required: The Gemini model to use
MODEL_NAME=gemini-2.0-flash-exp
```

### 4. Authenticate with Google Cloud

If using Vertex AI (recommended):

```bash
gcloud auth application-default login
```

If using Gemini API instead, add your API key to the `.env` file:

```bash
GOOGLE_API_KEY=your-api-key-here
```

## Running the Agent

### Option 1: Command Line Interface (CLI)

Run the agent in your terminal:

```bash
adk run shopping_concierge
```

### Option 2: Web Interface

Start the web interface:

```bash
adk web
```

Then open your browser to the URL shown (typically `http://localhost:8000`) and select `shopping_concierge` from the dropdown menu.

## Project Structure

```
shopping-concierge/
├── shopping_concierge/          # Main agent code
│   ├── __init__.py             # Package initialization
│   ├── agent.py                # Core agent logic
│   ├── prompt.py               # Agent prompts and instructions
│   └── tools/                  # Custom tools for the agent
├── tests/                      # Unit tests
├── eval/                       # Evaluation scripts and data
├── deployment/                 # Deployment scripts
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore file
├── pyproject.toml             # Project configuration
└── README.md                  # This file
```

## Development

### Running Tests

```bash
uv sync --dev
uv run pytest tests
```

### Running Evaluations

```bash
uv run pytest eval
```

## Customization

To customize the agent for your specific use case:

1. **Modify Agent Behavior**: Edit `shopping_concierge/agent.py` to change the agent's logic
2. **Update Prompts**: Edit `shopping_concierge/prompt.py` to customize instructions
3. **Add Custom Tools**: Create new tools in `shopping_concierge/tools/`
4. **Configure Models**: Update the `MODEL_NAME` in your `.env` file

## Deployment

### Deploy to Vertex AI Agent Engine

1. Build the wheel file:

```bash
uv build --wheel --out-dir deployment
```

2. Deploy the agent:

```bash
cd deployment
uv run python deploy.py
```

Note: Deployment may take 10+ minutes to complete.

## Example Interactions

Here are some example queries you can try:

- "I'm looking for a gift for my tech-savvy friend who loves gadgets"
- "Can you help me find a comfortable office chair under $300?"
- "I need running shoes for marathon training"
- "What's a good laptop for video editing?"

## Troubleshooting

### Common Issues

**Issue**: Authentication errors when running the agent

**Solution**: Make sure you've run `gcloud auth application-default login` and your Google Cloud project has the Vertex AI API enabled.

**Issue**: Module not found errors

**Solution**: Ensure you've installed dependencies with `uv sync`.

**Issue**: Environment variable errors

**Solution**: Check that your `.env` file exists and contains all required variables from `.env.example`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache 2.0 License.

## Acknowledgements

Built with [Google's Agent Development Kit (ADK)](https://google.github.io/adk-docs/).

## Disclaimer

This agent is provided for demonstration purposes only and is not intended for production use without proper testing, security hardening, and customization for your specific use case.
