#!/usr/bin/python3
"""UTF-8 validation module."""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Check if data is valid UTF-8 encoding.

    In UTF-8 encoding data that can be
    represented with a single byte (8-bits)
    is usually in encoded by adding a leading
    zero followed by the 7-bit ASCII value
    of the character ie 01000001 = 'A' in UTF-8.

    In multi-bytes characters, i.e. numbers
    that can not be represented in traditional
    7-bit ASCII, special rules apply.

    For 2-byte characters, the first byte contains
    the sequence '110xxxxx' the first three
    most significant bits denote that it a two-byte character
    and the remaining five bits represent a binary number
    and the second byte has the sequence '10xxxxxx' where
    the first two most significant bits ('10') denote
    that it's a continuation of a character
    .i.e. data = [198, 178] ->[1100110, 10110010] corresponds
    to 434 character the first 3 bits of 198 denotes that it's a
    2-byte character and the firt two bits of 178 denote that it is
    a continuation of a character

    For three and four-byte characters, the first byte
    has the sequence '1110xxxx' and '11110xxx' respectively
    and to denote continuation of a character
    the sequence'10xxxxxx' still applies.

    args:
        data (list[int]): data to check if is validly encoded in UTF-8
    Return:
        True if the data is valid UTF-8 encoding else False

    """
    for i in range(len(data)):
        if (data[i] & 0b10000000) == 0:
            continue
        elif (data[i] & 0b11100000) == 0b11000000:
            if (data[i + 1] >= len(data)
               or (data[i + 1] & 0b11000000) != 0b10000000):
                return False
            continue
        elif (data[i] & 0b11110000) == 0b11100000:
            if (data[1 + 2] >= len(data)
               or any((data[i + j] & 0b11000000) != 0b10000000
               for j in range(1, 3))):
                return False
            continue
        elif (data[i] & 0b11111000) == 0b11110000:
            if (data[1 + 3] >= len(data)
               or any((data[i + j] & 0b11000000) != 0b10000000
               for j in range(1, 4))):
                return False
            continue
        else:
            return False
    return True
