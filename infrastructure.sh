#!/bin/bash
pip install uv
uv pip install browser-use
playwright install chromium --with-deps --no-shell
uv pip install crewai