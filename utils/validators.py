# utils/validators.py

from utils.errors import EmptySequenceError


def ensure_not_empty(sequence, msg: str = "Cannot operate on empty sequence.") -> None:
    """
    Raise an error if the sequence is empty.

    Args:
        seq: A list-like structure to check.
        msg: Optional custom error message.

    Raises:
        EmptySequenceError: If the sequence is empty.
    """
    if not sequence:
        raise EmptySequenceError(msg)
