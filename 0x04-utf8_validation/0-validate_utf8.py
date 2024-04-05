#!/usr/bin/python3
"""
Module for validating UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for num in data:
        # If the current byte is the start of a new character
        if num_bytes == 0:
            # Count the number of bytes in this UTF-8 character
            if (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            elif num >> 7:
                return False
        else:
            # If the byte does not start with
            # 10xxxxxx, it's not a valid continuation byte
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If there are leftover bytes, it means the
    # data is incomplete
    return num_bytes == 0
