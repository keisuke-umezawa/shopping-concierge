#!/bin/bash
set -e

echo "🚀 Setting up Shopping Concierge development environment..."

# Install uv package manager
echo "📦 Installing uv package manager..."
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

# Verify uv installation
echo "✓ uv installed: $(uv --version)"

# Install project dependencies
echo "📚 Installing project & development dependencies..."
uv sync --dev

# Create .env file from example if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from .env.example..."
    cp .env.example .env
    echo "⚠️  Please update .env with your Google Cloud credentials"
fi

# Display helpful information
echo ""
echo "✅ Setup complete!"
echo ""
echo "📖 Quick Start Guide:"
echo "   1. Update .env with your Google Cloud Project ID and credentials"
echo "   2. Run 'adk run shopping_concierge' to start the CLI"
echo "   3. Run 'adk web' to start the web interface"
echo "   4. Run 'uv run pytest tests' to run tests"
echo ""
echo "🔐 Authentication:"
echo "   For Vertex AI: Run 'gcloud auth application-default login'"
echo "   For Gemini API: Add GOOGLE_API_KEY to .env"
echo ""
