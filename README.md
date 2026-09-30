# CryptoTractatusMVP

The fourth and final stage of my classical cryptography experiments, developed in June 2025.

This version followed the more architecture-heavy `Crypto-Tractatus` project and moved back toward a smaller, usable command-line application.

It experiments with:

- config-driven CLI commands
- reusable cipher components
- ROT, Caesar-style substitution and Vigenère
- English and Swedish alphabets
- case-preserving substitution
- punctuation-aware text handling
- composable cipher pipelines

## Installation

```bash
pip install -r requirements.txt
```

## Usage

ROT:

```bash
python3 -m cli.main encrypt rot \
  --text "Hello, World" \
  --shift 3 \
  --lang en
```

Output:

```text
Khoor, Zruog
```

Vigenère:

```bash
python3 -m cli.main encrypt vigenere \
  --text "ATTACK AT DAWN" \
  --keyword LEMON \
  --lang en
```

Output:

```text
LXFOPV EF RNHR
```

Lowercase keywords are normalized automatically, and letter case is preserved in the transformed text.

## Verification

```bash
make check
```

The restored project currently has regression coverage for:

- ROT encryption and round trips
- Vigenère encryption and decryption
- repeated characters in Vigenère keywords
- classical Vigenère key advancement over letters only
- mixed-case input
- punctuation preservation
- CLI execution
- English and Swedish alphabets

## Project lineage

1. `crypto_lab`
2. `crypto_proto_1`
3. `Crypto-Tractatus`
4. `CryptoTractatusMVP`

## Historical restoration

The original project has been kept largely intact. Small fixes were made to restore its intended behavior:

- removed stale CLI operations
- prevented config metadata from becoming CLI commands
- restored Vigenère CLI configuration
- preserved repeated characters in Vigenère keywords
- normalized English and Swedish cipher alphabets to uppercase
- preserved letter case and punctuation in substitution ciphers
- advanced the Vigenère key on letters only, matching the classical cipher
- declared the project's runtime dependencies
- added regression tests and a simple verification command

## License

MIT

## Status

Historical project. Archived as the final step in the CryptoTractatus learning series.
