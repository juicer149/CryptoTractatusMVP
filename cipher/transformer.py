from typing import Sequence, List
from cipher.base import CipherBit

class CipherTransformer:
    """
    Executes one or more CipherBit objects in sequence, transforming the text through a pipeline.

    This mimics Unix-style piping: each CipherBit takes the output of the previous as input.
    """

    def __init__(self, ciphers: Sequence[CipherBit]):
        if not ciphers:
            raise ValueError("Pipeline must contain at least one CipherBit.")
        self.pipeline: List[CipherBit] = list(ciphers)

    def run(self, mode: str = "encrypt") -> List[str]:
        """
        Run the transformation pipeline in the given mode.

        Args:
            mode (str): Either 'encrypt' or 'decrypt'.

        Returns:
            List[str]: The final transformed text.
        """
        if mode not in {"encrypt", "decrypt"}:
            raise ValueError("Mode must be 'encrypt' or 'decrypt'.")

        text = self.pipeline[0].text
        for cipher in self.pipeline:
            cipher.text = text  # rebind input for next cipher
            text = cipher.encrypt() if mode == "encrypt" else cipher.decrypt()

        return text

    def __call__(self, mode: str = "encrypt") -> str:
        """
        Callable interface, returns joined string for user display.
        """
        return "".join(self.run(mode))
