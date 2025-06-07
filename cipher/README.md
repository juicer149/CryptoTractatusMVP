# CryptoTractatus – Cipher Core

This module contains the cryptographic core components of **CryptoTractatus** — a framework for classical cipher experimentation and analysis.

---

## Design Principles

- **Composable**: All ciphers inherit from a common base (`CipherBit`).
- **Minimal**: No external dependencies beyond Python stdlib.
- **Purity**: Most functions are deterministic and side-effect-free.
- **Fallbacks**: Fast path support (e.g., `rot_text`) for performance-critical use cases.

---

## Module Overview

| File             | Description                                                              |
|------------------|--------------------------------------------------------------------------|
| `base.py`        | Abstract base class for all ciphers (`CipherBit`)                        |
| `rot.py`         | Implementation of ROT (Caesar) cipher                                     |
| `charmap.py`     | Character mapping utility used by many substitution-based ciphers         |

---

## Base Class: `CipherBit`

All ciphers must subclass `CipherBit`:

```python
@dataclass
class CipherBit(ABC):
    text: List[str]
    alphabet: List[str]
    fast: bool = False

    def __call__(self, mode: str) -> List[str]
    def encrypt(self) -> List[str]
    def decrypt(self) -> List[str]
```

The `__call__` method dispatches based on mode (`encrypt` or `decrypt`).

---

## Utility: `CharMap`

The `CharMap` class offers deterministic character substitution with fallbacks. It supports:

- `CharMap.from_lists(keys, values)`: simple 1:1 mapping
- `CharMap.from_generator(...)`: for polyalphabetic systems like Vigenère
- Callable usage: `mapping(['A', 'B', 'C'])`

---

## Example: Creating a New Cipher

1. **Create a new file** in `cipher/`, e.g. `vigenere.py`
2. **Inherit from** `CipherBit`
3. **Implement** `encrypt()` and `decrypt()` using `CharMap`, `rotate`, or your own logic

```python
@dataclass(kw_only=True)
class VigenereCipher(CipherBit):
    keyword: str

    def encrypt(self) -> List[str]:
        # implement using self.keyword and self.alphabet
        pass

    def decrypt(self) -> List[str]:
        # implement inverse
        pass
```

4. Add optional fast-path support if needed (`self.fast`).

---

## Integration with CLI

Once the cipher is defined:
- Register it in `cli/commands/` via `@register_command`
- Add its config to `cli/config/`
- No need to touch parser or dispatch logic

---

## Philosophy

This module treats ciphers as **pure transformations** over character sequences. The emphasis is on:
- **Clarity over cleverness**
- **Data over control structures**
- **Reusability via composition**

