#!/bin/bash

# Quality
black dabeplech/
pydocstyle dabeplech/
flake8 --max-complexity=10 --max-line-length=127 dabeplech/

# Tests
pytest tests/
