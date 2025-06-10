# CryptoTractatus — Cipher Core

This directory contains the cryptographic core of **CryptoTractatus**, a framework for experimenting with and analyzing classical ciphers.

---

## Design Principles

- **Composable**: All ciphers subclass a common base (`CipherBit`).
- **Minimal**: Only Python's standard library is required.
- **Pure**: Functions are deterministic and avoid side effects.
- **Performance**: Optional "fast path" support for speed-critical operations.

---

## Module Structure

| File                | Description                                                        |
|---------------------|--------------------------------------------------------------------|
| `base.py`           | Abstract base class for ciphers (`CipherBit`)                      |
| `charmap.py`        | Deterministic character mapping utility (substitution ciphers)      |
| `charmap_table.py`  | Table for polyalphabetic or keyed substitution systems             |
| `interfaces.py`     | Cipher table interface abstraction                                 |
| `monoalphabetic.py` | Monoalphabetic cipher implementation                               |
| `transformer.py`    | Pipeline for chaining multiple ciphers                             |
| `vigenere.py`       | Vigenère cipher implementation                                     |

---

## Base Class: `CipherBit`

All ciphers subclass `CipherBit`, which standardizes the interface for encryption and decryption:

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

- The `__call__` method dispatches to `encrypt` or `decrypt` based on the given mode.
- Subclasses must implement `encrypt()` and `decrypt()`.

---

## Utility: `CharMap`

`CharMap` provides deterministic character substitution with fallbacks.

- `CharMap.from_lists(keys, values)`: create a 1:1 mapping.
- `CharMap.from_generator(...)`: create mappings for polyalphabetic systems (e.g., Vigenère).
- Callable: `mapping(['A', 'B', 'C'])` applies the mapping.

---

## Example: Creating a New Cipher

To add a new cipher:

1. **Create a new file** in `cipher/`, for example `mycipher.py`.
2. **Inherit from** `CipherBit`.
3. **Implement** `encrypt()` and `decrypt()`.

```python
@dataclass(kw_only=True)
class MyCipher(CipherBit):
    custom_param: str

    def encrypt(self) -> List[str]:
        # Implement encryption logic
        pass

    def decrypt(self) -> List[str]:
        # Implement decryption logic
        pass
```

4. Optionally, add fast-path logic if needed.

---

## Integration with CLI

After defining a cipher:

- Register it in `cli/commands/` with `@register_command`.
- Add its configuration YAML to `cli/config/`.
- No edits to parser or dispatch logic are needed.

---

## Philosophy

Ciphers are treated as **pure transformations** over character sequences.

- **Clarity** over cleverness
- **Data-centric** design
- **Composable** abstractions

---

## See Also

- [cli/commands/](../cli/commands/) — Command integration layer
- [cli/config/](../cli/config/) — Cipher configuration files
