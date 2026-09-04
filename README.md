# pyextract

Small dependency-free helpers for extracting useful values from Python mappings and sequences.

## Features

- Nested key lookup
- Safe path extraction
- First-match extraction
- Clear defaults for missing data

## Usage

```python
from pyextract import get_path

value = get_path({"user": {"name": "medu"}}, "user.name")
print(value)
```

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

https://guns.lol/meduu
