# Language Module – Unicode Alphabet Tools

This module provides language-specific Unicode alphabets for use in classical ciphers.
It supports loading, generation, and fallbacks for A–Z and custom characters (e.g., ÅÄÖ).

---

## Structure

```
language/
├── tools.py       # Core logic for alphabet loading and generation
└── alphabets/     # YAML alphabet definitions (e.g., en.yaml, sv.yaml)
```

---

## Functions

### `load_unicode_alphabet(lang: str = "en") -> List[str]`

Loads a YAML alphabet given a language code.

- If no file exists, falls back to A–Z.
- Supports:
  - Unicode ranges (start, end)
  - Extras (custom characters like å, ä, ö)

### `generate_unicode_yaml(name: str, start: int, end: int, extras: List[str] = None, out_dir: Path = ALPHABET_DIR)`

Creates a YAML file in `alphabets/` for a given language.

Usage example:
```python
generate_unicode_yaml("sv", 65, 91, extras=["Å", "Ä", "Ö"])
```

Output:
```yaml
range:
  start: 65
  end: 91
  name: sv
extras:
  Å: 197
  Ä: 196
  Ö: 214
```

### `basic_unicode_latin() -> List[str]`

Returns default uppercase Latin alphabet: A–Z.

---

## How to Add New Alphabets

1. Use `generate_unicode_yaml()` in Python shell or script:
```python
from language.tools import generate_unicode_yaml

generate_unicode_yaml("el", 913, 938)  # Greek uppercase
```

2. Alphabet becomes accessible via:
```python
load_unicode_alphabet("el")
```

---

## Design Principles

- YAML-based declarative alphabets
- Unicode-safe and language-agnostic
- Extendable via CLI or code
- Separation of data (YAML) and logic (Python)

This module is central to how CryptoTractatus adapts to multilingual contexts and user-defined ciphers.

