# OOP

The repo contains implementations of certain programming patterns for Object-Oriented Programming.

## For Consumers

### Installation

```bash
python3.<bootstrap-pytho-minor> -m venv .venv
source .venv/bin/activate
```

## For Developers

### Cloning the project

Execute the following commands:
```bash
git clone https://github.com/ABKorotky/oop.git
cd oop
```

### Prepare a virtual environment

Execute the following commands:
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Prepare repository hooks

Execute the following commands:
```bash
pre-commit autoupdate
pre-commit install
```
