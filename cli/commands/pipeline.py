from cli.registry import register_command
from cipher.vigenere import Vigenere
from cipher.monoalphabetic import MonoalphabeticCipher
from cipher.charmap_table import CharmapTable
from cipher.transformer import CipherTransformer
from utils.alphabet_loader import load_alphabet

@register_command("encrypt", "pipeline")
def pipeline_encrypt(args):
    ciphers = []
    alphabet = load_alphabet(args.lang)
    table = CharmapTable.from_alphabet(alphabet, source="cli")
    if args.use_vigenere:
        ciphers.append(Vigenere(
            text=list(args.text),
            keyword=list(args.keyword),
            alphabet=alphabet,
            table=table
        ))
    if args.use_mono:
        ciphers.append(MonoalphabeticCipher(
            text=list(args.text),
            key_char=args.key_char,
            alphabet=alphabet,
            table=table
        ))
    pipeline = CipherTransformer(ciphers)
    return pipeline("encrypt")
