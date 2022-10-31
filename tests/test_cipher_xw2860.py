from cipher_xw2860 import cipher_xw2860
import pytest

# Test function for single word

def test_single_cipher():
    example = 'Test'
    expected = 'Yjxy'
    actual = cipher_xw2860.cipher(example, 5)
    assert actual == expected

    