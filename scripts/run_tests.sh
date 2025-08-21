#!/usr/bin/env bash
set -euo pipefail

# Run lint + tests locally. Uses a throwaway venv so your system stays clean.

PY=${PYTHON:-python3}
WORKDIR=$(cd "$(dirname "$0")/.." && pwd)
cd "$WORKDIR"

VENV=".venv"
if [ ! -d "$VENV" ]; then
    "$PY" -m venv "$VENV"
fi

# Activate virtual environment
source "$VENV/bin/activate"

# Upgrade pip silently
python -m pip install --upgrade pip >/dev/null

# Install dependencies
pip install -r requirements.txt

echo -e "\n== flake8 =="
flake8 src tests

# Ensure reports directory exists
mkdir -p reports

echo -e "\n== pytest =="
pytest -q --junitxml=reports/junit.xml

echo -e "\nAll good ✅"
