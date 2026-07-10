# CI/CD Pipeline — Telecom Tax Calculator & Selenium UI Test

![CI](https://github.com/bekucukakin/i2i-Academy-ContinuousIntegrationContinuousDeploymentPipelines-16/actions/workflows/ci-cd.yml/badge.svg)

A small GitHub Actions pipeline that runs a unit test and a headless Selenium UI test on every
push, then prints a simulated deployment confirmation only when both tests pass.

## Project structure

```
.
├── .github/
│   └── workflows/
│       └── ci-cd.yml             GitHub Actions pipeline definition
├── src/
│   ├── __init__.py               Marks src as a Python package
│   └── telecom_tax.py            Telecom tax calculation logic
├── tests/
│   ├── test_telecom_tax.py       Unit test for the tax calculator
│   └── test_ui_selenium.py       Headless Selenium UI test
├── requirements.txt              Pinned project dependencies
├── .gitignore
└── README.md
```

## What it does

- **`calculate_total_with_taxes`** takes a raw amount and returns the total after adding a
  special communication tax (7.5%) and VAT (20%). It raises a `ValueError` for negative amounts.
  The rates are sample values chosen for this exercise, not current official tax figures.
- **Unit test** verifies that `100` correctly becomes `127.5` after tax.
- **Selenium test** launches headless Chrome, opens `https://example.com`, and asserts the page
  title is `"Example Domain"`.

## Pipeline

On every push, `.github/workflows/ci-cd.yml` runs on `ubuntu-latest` and executes, in order:

1. Checkout the repository
2. Set up Python 3.12
3. Install dependencies from `requirements.txt`
4. Run the unit test
5. Run the Selenium UI test
6. Print a simulated deployment confirmation message

If either test fails, GitHub Actions stops the job automatically, so the deployment message is
only ever printed when both tests have passed.

## Running locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m pytest -v
```

## Tech stack

- Python 3.12
- pytest 9.1.1
- Selenium 4.45.0
- GitHub Actions
