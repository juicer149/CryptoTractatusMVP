from cli.registry import register_command
from cipher.vigenere import Vigenere
from cipher.charmap_table import CharmapTable
from cipher.transformer import CipherTransformer
from utils.alphabet_loader import load_alphabet

@register_command("encrypt", "vigenere")
def vigenere_encrypt(args):
    alphabet = load_alphabet(args.lang)  # eller "en", eller Path(...)
    table = CharmapTable.from_alphabet(alphabet, source="cli")
    cipher = Vigenere(
        text=list(args.text),
        keyword=list(args.keyword),
        alphabet=alphabet,
        table=table
    )
    pipeline = CipherTransformer([cipher])
    return pipeline("encrypt")

@register_command("decrypt", "vigenere")
def vigenere_decrypt(args):
    alphabet = load_alphabet(args.lang)
    table = CharmapTable.from_alphabet(alphabet, source="cli")
    cipher = Vigenere(
        text=list(args.text),
        keyword=list(args.keyword),
        alphabet=alphabet,
        table=table
    )
    pipeline = CipherTransformer([cipher])
    return pipeline("decrypt")
