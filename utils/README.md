# `utils/` – Utility Modules for CryptoTractatus

This directory contains generic utilities used throughout the CryptoTractatus project. The modules are grouped into four key areas:

- **Validation**
- **Functional tools**
- **Quick fallback algorithms**
- **Error handling**

These tools are pure, minimal, and built with Unix-style composability in mind.

---

## Overview

| File            | Purpose                                              |
| --------------- | ---------------------------------------------------- |
| `tools.py`      | Pure sequence transformations (e.g. rotate, dedupe)  |
| `quick.py`      | Optimized one-shot utilities (e.g. Caesar fallback)  |
| `validators.py` | Precondition checks and value assertions             |
| `errors.py`     | Custom error classes for internal exception handling |
| `load.py`       | Minimal I/O functions for YAML and JSON parsing      |
| `alphabet_loader.py` | Robust alphabet loading from YAML or language   |

---

## Usage Examples

### Rotation Logic (Pure)

```python
from utils.tools import rotate
rotate("ABCDEF", -2)  # ["C", "D", "E", "F", "A", "B"]
```

### Fallback Caesar Encrypt

```python
from utils.quick import rot_text
rot_text("HELLO", 3, lang="en")  # "KHOOR"
```

### Load Config

```python
from utils.load import load_yaml
config = load_yaml(Path("config/rot.yaml"))
```

### Ensure Non-Empty Input

```python
from utils.validators import ensure_not_empty
ensure_not_empty([1,2,3])  # OK
ensure_not_empty([])       # Raises EmptySequenceError
```

---

## Extending

These modules are intended to remain low-level and side-effect free:

- Do **not** introduce cipher-specific logic here
- Prefer list/iterable interfaces
- Raise **custom errors**, never built-ins

If you want to add new validators or helpers, follow these guidelines:

- **tools.py** – Only pure transformations (e.g., strip accents, remove symbols)
- **validators.py** – Always raise `CryptoTractatusError` subclasses
- **quick.py** – Stateless cipher fallbacks (no classes, just functions)
- **load.py** – Only load/save logic (no interpretation or transformation)

---

## Error Classes

Use these to provide better internal traceability:

| Error Class                  | Raised When                                    |
| ---------------------------- | ---------------------------------------------- |
| `CryptoTractatusError`       | Base class for all internal errors             |
| `EmptySequenceError`         | Sequence operation is called on an empty input |
| `MappingLengthMismatchError` | Two lists to be zipped differ in length        |
| `UnknownCommandError`        | CLI dispatch fails to find a matching command  |

---

## Philosophy

The `utils/` layer embodies the philosophy of CryptoTractatus:

- Keep abstractions minimal
- Code should be testable without mocks or side effects
- Let high-level systems orchestrate behavior, not helpers
- Avoid assumptions or implicit defaults

This allows you to build robust crypto primitives and command-line tools atop a stable, predictable foundation.

