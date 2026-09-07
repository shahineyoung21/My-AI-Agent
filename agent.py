name: Run AI Agent

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  run-agent:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install google-generativeai

    - name: Run Agent
      run: python main.py
