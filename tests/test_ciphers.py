import unittest

from cipher.charmap_table import CharmapTable
from cipher.vigenere import Vigenere
from utils.alphabet_loader import load_alphabet


class VigenereTests(unittest.TestCase):
    def test_vigenere_key_example(self):
        alphabet = load_alphabet("en")
        table = CharmapTable.from_alphabet(alphabet, source="test")

        cipher = Vigenere(
            text=list("HELLO"),
            alphabet=alphabet,
            keyword=list("KEY"),
            table=table,
        )

        self.assertEqual("".join(cipher.encrypt()), "RIJVS")

    def test_vigenere_repeated_keyword_characters(self):
        alphabet = load_alphabet("en")
        table = CharmapTable.from_alphabet(alphabet, source="test")

        cipher = Vigenere(
            text=list("HELLO"),
            alphabet=alphabet,
            keyword=list("BOOK"),
            table=table,
        )

        encrypted = cipher.encrypt()
        self.assertEqual("".join(encrypted), "ISZVP")

        decrypted = Vigenere(
            text=encrypted,
            alphabet=alphabet,
            keyword=list("BOOK"),
            table=table,
        ).decrypt()

        self.assertEqual("".join(decrypted), "HELLO")

    def test_swedish_vigenere_round_trip(self):
        alphabet = load_alphabet("sv")
        table = CharmapTable.from_alphabet(alphabet, source="test")

        encrypted = Vigenere(
            text=list("HEJÅÄÖ"),
            alphabet=alphabet,
            keyword=list("NYCKEL"),
            table=table,
        ).encrypt()

        decrypted = Vigenere(
            text=encrypted,
            alphabet=alphabet,
            keyword=list("NYCKEL"),
            table=table,
        ).decrypt()

        self.assertEqual("".join(decrypted), "HEJÅÄÖ")


class AlphabetTests(unittest.TestCase):
    def test_english_alphabet(self):
        self.assertEqual(
            "".join(load_alphabet("en")),
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        )

    def test_swedish_alphabet(self):
        self.assertEqual(
            "".join(load_alphabet("sv")),
            "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ",
        )


if __name__ == "__main__":
    unittest.main()
