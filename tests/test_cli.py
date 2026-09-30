import subprocess
import sys
import unittest


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        result = subprocess.run(
            [sys.executable, "-m", "cli.main", *args],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()

    def test_rot_encrypt(self):
        self.assertEqual(
            self.run_cli(
                "encrypt",
                "rot",
                "--text",
                "HELLO",
                "--shift",
                "3",
                "--lang",
                "en",
            ),
            "KHOOR",
        )

    def test_rot_round_trip_swedish(self):
        encrypted = self.run_cli(
            "encrypt",
            "rot",
            "--text",
            "HEJÅÄÖ",
            "--shift",
            "3",
            "--lang",
            "sv",
        )

        decrypted = self.run_cli(
            "decrypt",
            "rot",
            "--text",
            encrypted,
            "--shift",
            "3",
            "--lang",
            "sv",
        )

        self.assertEqual(decrypted, "HEJÅÄÖ")

    def test_vigenere_encrypt(self):
        self.assertEqual(
            self.run_cli(
                "encrypt",
                "vigenere",
                "--text",
                "HELLO",
                "--keyword",
                "KEY",
                "--lang",
                "en",
            ),
            "RIJVS",
        )

    def test_vigenere_repeated_keyword(self):
        encrypted = self.run_cli(
            "encrypt",
            "vigenere",
            "--text",
            "HELLO",
            "--keyword",
            "BOOK",
            "--lang",
            "en",
        )

        self.assertEqual(encrypted, "ISZVP")

        decrypted = self.run_cli(
            "decrypt",
            "vigenere",
            "--text",
            encrypted,
            "--keyword",
            "BOOK",
            "--lang",
            "en",
        )

        self.assertEqual(decrypted, "HELLO")


if __name__ == "__main__":
    unittest.main()
