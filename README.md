# OO Patterns

The repo contains implementations of certain programming patterns for Object-Oriented Programming.

## For Consumers

### Installation

1. Create and activate a virtual environment if not exists:
```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

2. Install the package:
```bash
pip install ak-oo-patterns
```

## For Developers

### Cloning the project

Run the following commands:
```bash
git clone https://github.com/ABKorotky/oop.git
cd oop
```

### Prepare a virtual environment

Run the following commands:
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Prepare repository hooks

Run the following commands:
```bash
pre-commit autoupdate
pre-commit install
```

### Using `tox` tool

The repo has a configuration for well-known `tox` tool. It allows to automate some developer activities.
Run the following command for getting help:
```bash
tox list
```
Output example is:
```bash
default environments:
cs     -> Checks code style by black, isort and flake8 tools
ann    -> Checks types annotations by mypy
utc    -> Runs tests under coverage, prints a text report and builds HTML report

additional environments:
format -> Formats code by black and isort tools
doc    -> Generates documentation using sphinx tool
build  -> Builds PIP package using build tool
upload -> Uploads generated PIP package to PyPI index
```
