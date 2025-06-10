from cipher.monoalphabetic import MonoalphabeticCipher
from cipher.charmap_table import CharmapTable
from utils.alphabet_loader import load_alphabet
from utils.tools import remove_duplicates

def run_mono_variant(args, mode, variant):
    """
    Generic handler for monoalphabetic cipher variants.
    :param args: CLI arguments namespace
    :param mode: "encrypt" or "decrypt"
    :param variant: One of "rot", "caesar", "keywordmono", "mono"
    :return: str (resulting ciphertext or plaintext)
    """
    alphabet = load_alphabet(getattr(args, "lang", None))

    if variant == "rot":
        key_char = alphabet[args.shift % len(alphabet)]
        mono_alphabet = alphabet
        table = CharmapTable.from_alphabet(mono_alphabet, source="cli")
    elif variant == "caesar":
        key_char = alphabet[3 % len(alphabet)]
        mono_alphabet = alphabet
        table = CharmapTable.from_alphabet(mono_alphabet, source="cli")
    elif variant == "keywordmono":
        keyword = list(args.keyword)
        mono_alphabet = remove_duplicates(keyword) + [c for c in alphabet if c not in keyword]
        key_char = alphabet[0]
        # Here, map the plain alphabet to the keyword-based mono_alphabet
        table = CharmapTable.from_plain_and_cipher_alphabet(alphabet, mono_alphabet, source="cli")
    elif variant == "mono":
        key_char = args.key_char
        mono_alphabet = alphabet
        table = CharmapTable.from_alphabet(mono_alphabet, source="cli")
    else:
        raise ValueError(f"Unknown mono variant: {variant}")

    cipher = MonoalphabeticCipher(
        text=list(args.text),
        key_char=key_char,
        alphabet=mono_alphabet,
        table=table
    )
    func = getattr(cipher, "encrypt" if mode == "encrypt" else "decrypt")
    return "".join(func())
