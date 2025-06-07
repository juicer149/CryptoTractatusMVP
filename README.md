# CryptoTractatus – Project Overview

CryptoTractatus is a modular, Unix-inspired toolkit for classical cryptography. It emphasizes composability, readability, and extensibility. The project combines cryptographic primitives, language-aware tooling, and a minimal but powerful CLI interface for transformation and analysis.

---

## Project Structure

```
CryptoTractatus_demo/
├── cipher/             # Cipher core logic and base abstractions
├── cli/                # Command-line interface architecture
├── language/           # Language-aware alphabet loaders and utilities
└── utils/              # Shared utility functions and validators
```

---

## Component Overview

### `cipher/`

* **`base.py`**: Abstract base class `CipherBit` for pluggable cipher components
* **`rot.py`**: ROT cipher implementation
* **`charmap.py`**: Mapping layer for symbol substitution

### `cli/`

* **`main.py`**: Entrypoint
* **`parser.py`**: Builds CLI parser from YAML configs
* **`dispatch.py`**: Dynamic handler routing
* **`registry.py`**: Decorator-based command registration
* **`commands/`**: One file per cipher (e.g., `rot.py`)
* **`config/`**: Operation-specific YAML flag definitions and default settings

### `language/`

* **`tools.py`**: Unicode-aware alphabet loader from YAML specs
* **`alphabets/`**: Language YAML files (e.g., `en.yaml`, `sv.yaml`)

### `utils/`

* **`tools.py`**: Pure functions like `rotate`, `zip_to_dict`
* **`quick.py`**: Fast CLI-friendly shortcuts
* **`validators.py`**: Input guards
* **`errors.py`**: Custom error hierarchy
* **`load.py`**: YAML/JSON file loaders

---

## CLI Flow Summary

1. `main.py` invokes `build_parser()`
2. `parser.py` loads flags from `config/*.yaml`
3. User input is parsed → dispatched via `dispatch.py`
4. Handlers are mapped via `@register_command`
5. Cipher instance is built, executed, and outputs transformed text

---

## Adding a Cipher

1. Add a config YAML in `cli/config/`
2. Implement cipher class in `cipher/`
3. Register handlers in `cli/commands/`

No core logic needs modification due to config-driven + registry-based design.

---

## Example Usage

```bash
cryptotractatus encrypt rot --text "HELLO" --shift 3
```

---

## Philosophy

* Minimalistic, testable components
* Explicit config separation
* Rich Unicode + language support
* CLI-first design with Unix sensibilities

---

For module-specific details, see individual `README.md` files in each directory.

