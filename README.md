# FDE Screening

Author: Klaus Begnis

## Requirements

You may install requirements through

```
uv add pytest
```

Or with directly with pip

```
pip install pytest
```

## Test converage

Scenarios for each type of classification can be check running:


Test coverage:
- Valid packages (possible dimensions and mass)
- Invalid packages (impossible dimensions or mass)


```
uv run pytest tests.py
```

or

```
python3 pytest tests.py
```
## Future mprovements

- Segment the bulky and heavy classification into new methods
