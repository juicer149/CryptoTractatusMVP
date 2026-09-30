# CryptoTractatusMVP

The fourth and final stage of my classical cryptography experiments, developed in June 2025.

This version followed the more architecture-heavy `Crypto-Tractatus` project and moved back toward a smaller, usable command-line application.

It experiments with:

- config-driven CLI commands
- reusable cipher components
- ROT, Caesar-style substitution and Vigenère
- English and Swedish alphabets
- composable cipher pipelines

## Usage

```bash
python3 -m cli.main encrypt rot \
  --text HELLO \
  --shift 3 \
  --lang en

python3 -m cli.main encrypt vigenere \
  --text HELLO \
  --keyword KEY \
  --lang en
```

## Verification

```bash
make check
```

The restored project currently has regression coverage for ROT, Vigenère, repeated-key characters, CLI execution, and English/Swedish alphabets.

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
- added regression tests and a simple verification command

## Status

Historical project. Archived as the final step in the CryptoTractatus learning series.
