# cli/run.py

import sys
import inquirer

from cli.dispatch import dispatch
from cli.parser import build_parser
import cli.commands.rot 

def run_interactive():
    # 1. Hämta tillgängliga ciphers och operationer
    parser = build_parser()
    cipher_choices = ["rot"]  # Fyll på med fler vid behov, ev läs dessa från en konfigfil
    op_choices = ["encrypt", "decrypt"]

    # 2. Fråga användaren
    op = inquirer.list_input("Vad vill du göra?", choices=op_choices)
    cipher = inquirer.list_input("Vilken cipher?", choices=cipher_choices)

    # 3. Dynamiskt fråga efter parametrar beroende på cipher
    questions = []
    if cipher == "rot":
        questions.append(inquirer.Text("shift", message="Shift (t.ex. 3)"))
    questions.append(inquirer.Text("text", message="Text att transformera"))
    questions.append(inquirer.Text("lang", message="Språk (default: en)", default="en"))

    answers = inquirer.prompt(questions)

    # 4. Bygg sys.argv-liknande lista och dispatcha
    sys.argv = [
        sys.argv[0],
        op,
        cipher,
        "--text", answers["text"],
        "--shift", answers["shift"],
        "--lang", answers["lang"]
    ]
    args = parser.parse_args()
    result = dispatch(args)
    print("\nResultat:", "".join(result))


if __name__ == "__main__":
    run_interactive()
