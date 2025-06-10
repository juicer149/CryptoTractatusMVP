# CryptoTractatus – Project Overview

CryptoTractatus is a modular, Unix-inspired toolkit for classical cryptography.  
It emphasizes composability, readability, and extensibility. The project combines cryptographic primitives, language-aware tooling, and a minimal but powerful CLI interface for transformation and analysis.

---

## Project Structure

```
CryptoTractatus_demo/
├── cipher/             # Cipher core logic and base abstractions
├── cli/                # Command-line interface architecture and commands
├── language/           # Language-aware alphabet loaders and utilities
└── utils/              # Shared utility functions and validators
```

---

## Component Overview

### `cipher/`

- **`base.py`**: Abstract base class `CipherBit` for pluggable cipher components
- **`monoalphabetic.py`**: Generic monoalphabetic cipher implementation (used for caesar, rot, mono, keywordmono)
- **`charmap.py`, `charmap_table.py`**: Mapping utilities for symbol substitution, supporting both simple and polyalphabetic ciphers
- **`vigenere.py`**: Vigenère cipher implementation
- **`transformer.py`**: Pipeline for chaining multiple ciphers
- **`interfaces.py`**: Shared interfaces for mapping tables and ciphers

### `cli/`

- **`main.py`**: CLI entrypoint (scriptable mode)
- **`run.py`**: Interactive CLI (question-based)
- **`parser.py`**: Builds CLI parser dynamically from YAML configs
- **`dispatch.py`**: Dynamic handler routing
- **`registry.py`**: Decorator-based command registration
- **`commands/`**: Handler modules, one per cipher variant (e.g., `caesar.py`, `rot.py`, `keywordmono.py`, etc.)
- **`config/`**: YAML files defining cipher flags and arguments per operation

### `language/`

- **`tools.py`**: Unicode-aware alphabet loader from YAML specs
- **`alphabets/`**: Language YAML files (e.g., `en.yaml`, `sv.yaml`) specifying Unicode ranges and custom chars

### `utils/`

- **`tools.py`**: Pure functions like `rotate`, `zip_to_dict`
- **`quick.py`**: Fast CLI-friendly shortcuts (e.g., quick Caesar/ROT fallback)
- **`validators.py`**: Input guards and assertions
- **`errors.py`**: Custom error hierarchy
- **`load.py`**: YAML/JSON file loaders
- **`alphabet_loader.py`**: Robust language/YAML-based alphabet loading helpers

---

## CLI Flow Summary

1. `main.py` or `run.py` invokes `build_parser()`
2. `parser.py` loads available operations and flags from `cli/config/*.yaml`
3. User input is parsed and dispatched via `dispatch.py`
4. Handlers are registered via `@register_command` decorators in `cli/commands/`
5. Correct cipher instance is built and executed, and transformed text is output

---

## Adding a Cipher

1. Add a config YAML in `cli/config/` describing arguments for your cipher
2. Implement the cipher class, or use an existing generic implementation in `cipher/`
3. Register handlers in `cli/commands/` (import into `main.py`/`run.py` if needed)
4. No core logic needs modification — config-driven and registry-based discovery

---

## Example Usage

**Scriptable CLI:**
```bash
cryptotractatus encrypt caesar --text "HELLO" --lang en
cryptotractatus encrypt rot --text "HELLO" --shift 13 --lang en
cryptotractatus encrypt keywordmono --text "HEJ" --keyword "KRYPTO" --lang sv
```

**Interactive CLI:**
```bash
python3 cli/run.py
```
- Step-by-step questions for operation, cipher, and parameters.

---

## Philosophy

- Minimalistic, testable components
- Explicit config separation (no hardcoded argument lists)
- Rich Unicode + language support (YAML alphabets, custom ranges)
- CLI-first design with Unix sensibilities

---

## Technical Debt & Limitations

- **Swedish alphabet output:** Currently, when using the Swedish alphabet (`sv`), the output for special letters such as Å, Ä, Ö is always in uppercase, regardless of the input casing. This is due to alphabet definition and casing handling in the current logic. Future improvements may allow preserving input casing.

- **Vigenère cipher:** The logic and class structure for Vigenère are implemented and tested, but some CLI integration and edge cases are still under development. The cipher is available for use, but minor bugs or missing features may exist.

- **General:** Some advanced cipher analysis features (like frequency analysis, auto-key, etc.) are planned but not yet implemented.
---

For module-specific details, see the `README.md` in each subdirectory.
