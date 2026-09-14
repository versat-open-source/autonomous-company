#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/../.."
project_python="${PROJECT_PYTHON:-.venv/bin/python}"
"$project_python" -m ruff format --check scripts tests
"$project_python" -m ruff check scripts tests
"$project_python" -m unittest discover -s tests -v
"$project_python" scripts/validate_project.py
