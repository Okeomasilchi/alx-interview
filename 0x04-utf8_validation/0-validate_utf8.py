#!/usr/bin/python3
"""
Module for validating UTF-8 encoding.
"""


def validUTF8(data):
    """
    Checks if the given list of integers represents a
    valid UTF-8 encoding.

    Args:
      data (list[int]): A list of integers representing
      bytes.

    Returns:
      bool: True if the given data represents a valid UTF-8
      encoding, False otherwise.
    """
    # Counter for bytes left in a multi-byte sequence
    bytes_remaining = 0

    for num in data:
        # Check the first byte (and any continuation bytes)
        byte = bin(num)[2:].zfill(8)  # Convert to 8-bit binary string

        if bytes_remaining == 0:  # Start of a new character sequence
            if byte[0] == "0":  # 1-byte character
                continue
            elif byte.startswith("110"):
                bytes_remaining = 1
            elif byte.startswith("1110"):
                bytes_remaining = 2
            elif byte.startswith("11110"):
                bytes_remaining = 3
            else:  # Invalid start byte
                return False
        else:  # Within a multi-byte sequence
            if not byte.startswith("10"):
                return False
            bytes_remaining -= 1

    return bytes_remaining == 0  # If all bytes processed successfully
