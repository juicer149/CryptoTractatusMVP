# CryptoTractatus – CLI Architecture

This directory contains the modular, extensible command-line interface (CLI) for CryptoTractatus — a toolkit for classical cryptography.

The CLI is designed for composability, configurability, and minimalism. Logic is separated from configuration, and new ciphers or operations can be added rapidly via YAML and Python modules.

---

## Structure Overview

| File/Dir             | Purpose                                                                 |
|----------------------|-------------------------------------------------------------------------|
| `main.py`            | CLI entrypoint — parses args and dispatches execution                   |
| `parser.py`          | Builds the argument parser from YAML config files                       |
| `dispatch.py`        | Routes execution to appropriate handlers based on parsed arguments      |
| `registry.py`        | Decorator-based command registration mechanism                          |
| `commands/`          | Handler modules for each cipher                                         |
| `config/`            | YAML files defining flags for each cipher and operation                 |
| `run.py`             | Interactive CLI (question-based) interface                              |

---

## Design Principles

- **Config-driven**: Cipher arguments (flags) are declared in YAML per cipher.
- **Composable**: New ciphers/operations can be added without modifying core logic.
- **Minimal dependencies**: Pure `argparse` and `inquirer` for interactive mode.
- **Unix mindset**: Each part is focused and testable.

---

## Usage

### Classic (scriptable) mode

Encrypting with ROT (shift 3):

```bash
cryptotractatus encrypt rot --text "HELLO" --shift 3
```

### Interactive CLI

Start the interactive CLI:

```bash
python3 cli/run.py
```

Example flow:

```
[?] Vad vill du göra?:
 > encrypt
   decrypt

[?] Vilken cipher?:
 > rot

[?] Shift (e.g., 3): 1
[?] Text att transformera: a b c
[?] Språk (default: en): en

Resultat: b c d
```

- **Shift** is prompted directly after the cipher is selected.
- Spaces and punctuation are left unchanged during encryption/decryption.
- Only letters are affected by the ROT cipher.

---

## Handling of Spaces and Punctuation

By default, only letters (`A-Z`, `a-z` — or their equivalents in the chosen alphabet) are included in the working alphabet for classical ciphers.
Other characters (spaces, punctuation, numbers) are **left unchanged** during transformation.

If you want to customize which characters are included/ignored, edit your alphabet YAML under `language/alphabets/`.

---

## Adding a New Cipher

To add a new cipher:

1. **YAML Config**
   - Create a file like `vigenere.yaml` in the `config/` folder.
   - Define flags per operation (e.g., `encrypt`, `decrypt`).

   Example:
   ```yaml
   common: &common_flags
     - name: "--keyword"
       type: str
       required: true
     - name: "--alphabet"
       type: str
     - name: "--lang"
       type: str

   encrypt: *common_flags
   decrypt: *common_flags
   analyze: []
   ```

2. **Command Handler**
   - Create `commands/vigenere.py`.
   - Register handlers with `@register_command("encrypt", "vigenere")` etc.
   - Use helpers for argument parsing and cipher instantiation.

3. **No Core Changes Needed** — parser, dispatch, and registry auto-discover ciphers.

---

## Example YAML Config

```yaml
common: &common_flags
  - name: "--shift"
    type: int
    required: true
  - name: "--alphabet"
    type: str
  - name: "--lang"
    type: str

encrypt: *common_flags
decrypt: *common_flags
analyze: []
```

---

## Internals

- Parsers are constructed dynamically from YAML
- Registry maps `(operation, cipher)` → handler function
- All text is treated as a list of characters before passing to the cipher core
- Interactive mode adapts questions per cipher choice

---

For internal API documentation, see `cipher/`, `language/`, and `utils/`.
