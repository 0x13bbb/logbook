#!/bin/bash

# Check Python version
REQUIRED_VERSION="3.12.3"
CURRENT_VERSION=$(python --version 2>&1 | cut -d' ' -f2)

if [ "$CURRENT_VERSION" != "$REQUIRED_VERSION" ]; then
    echo "Setting Python version to $REQUIRED_VERSION using pyenv..."
    pyenv local 3.12
    if [ $? -ne 0 ]; then
        echo "Failed to set Python version. Make sure pyenv is installed."
        exit 1
    fi
fi

# Navigate to backend directory
cd backend || exit 1

# Create and activate virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python -m venv .venv
fi

echo "Activating virtual environment..."
source .venv/bin/activate

# Install prerequisites
echo "Installing prerequisites..."
pip install -r requirements.txt

# Run the backend
echo "Starting FastAPI server..."
fastapi dev main.py