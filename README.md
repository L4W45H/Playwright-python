# PyPlaywrightProj

This project is a Python port of Playwright tests originally written in JavaScript.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install Playwright browsers:
   ```bash
   playwright install
   ```

## Running Tests

You can run all tests using pytest:
```bash
pytest
```

Or run a specific test file:
```bash
pytest test_slider.py
```

## Project Structure
- `pages/` - Page Object Model classes
- `test_*.py` - Test files 