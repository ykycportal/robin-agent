#!/bin/bash
# One-click setup script for Robin's AI Agent
# Usage: bash scripts/setup.sh

set -e

echo "======================================"
echo "🤖 Robin's AI Agent — Setup Script"
echo "======================================"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check Python
echo "📦 Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 not found${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Python3: $(python3 --version)${NC}"

# Check pip
echo "📦 Checking pip..."
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}❌ pip3 not found${NC}"
    exit 1
fi
echo -e "${GREEN}✅ pip3: $(pip3 --version | head -1)${NC}"

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate
echo -e "${GREEN}✅ Virtual environment created${NC}"

# Install core dependencies
echo ""
echo "📦 Installing core dependencies..."
pip install -q requests beautifulsoup4 lxml scrapling
echo -e "${GREEN}✅ Core libraries installed${NC}"

# Install optional dependencies
echo ""
echo "📦 Installing social media tools..."
pip install -q agent-reach
echo -e "${GREEN}✅ Agent-Reach installed${NC}"

echo ""
echo "📦 Installing app integrations..."
pip install -q composio
echo -e "${GREEN}✅ Composio installed${NC}"

# Setup config
echo ""
echo "⚙️  Setting up configuration..."
if [ ! -f ".env" ]; then
    cp config/.env.example .env
    echo -e "${YELLOW}⚠️  Created .env file — edit it to add API keys${NC}"
fi

# Verify installation
echo ""
echo "🔍 Verifying installation..."
python3 -c "import requests; print(f'✅ requests {requests.__version__}')"
python3 -c "from bs4 import BeautifulSoup; print('✅ beautifulsoup4')"
python3 -c "import lxml; print(f'✅ lxml {lxml.__version__}')"
python3 -c "from scrapling import Scrapling; print('✅ scrapling')"
python3 -c "import agent_reach; print(f'✅ agent-reach {agent_reach.__version__}')"
python3 -c "import composio; print(f'✅ composio {composio.__version__}')"

echo ""
echo "======================================"
echo "✅ Setup Complete!"
echo "======================================"
echo ""
echo "Next steps:"
echo "  1. Edit .env file and add your API keys"
echo "  2. Run: python examples/scrape_competitor.py"
echo "  3. Run: python examples/analyze_seo.py"
echo "  4. Run: python examples/monitor_social.py"
echo ""
echo "Documentation: docs/usage.md"
echo ""
