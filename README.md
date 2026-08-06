# IPL Data Project

A simple Python project for analyzing IPL match and delivery data.

## Project structure

- `src/` - Python scripts for computing IPL statistics.
- `data/` - CSV datasets used by the scripts.
- `tests/` - Unit tests for the analysis functions.
- `requirements.txt` - Python dependencies for running the project.

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Each module in `src/` exposes an `execute()` function and can also be run directly as a script.

Example:

```bash
python src/matches_played.py
```

By default, scripts use `data/matches.csv` and `data/deliveries.csv` as input files.

## Testing

Run the unit tests with:

```bash
python -m unittest discover -s tests
```
