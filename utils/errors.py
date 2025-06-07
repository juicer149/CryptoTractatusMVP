class CryptoTractatusError(Exception):
    """Bas-klass för alla anpassade fel i CryptoTractatus."""
    pass


class EmptySequenceError(CryptoTractatusError):
    """Raised when a sequence operation is attempted on an empty list."""
    def __init__(self, message="Cannot operate on an empty sequence."):
        super().__init__(message)


class MappingLengthMismatchError(CryptoTractatusError):
    """Raised when the length of a mapping does not match the expected length."""
    def __init__(self, messege= "Mapping length does not match expected length."):
        super().__init__(messege)


class UnknownCommandError(CryptoTractatusError):
    """Raised when a requested CLI command is not registered."""
    def __init__(self, operation: str, cipher: str):
        msg = f"Unknown command combination: operation='{operation}' cipher='{cipher}'"
        super().__init__(msg)

