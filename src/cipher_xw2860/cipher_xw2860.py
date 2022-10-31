def cipher(text, shift, encrypt=True):
    """"
    A function that encrypts text but replacing each letter by a letter that's a certain
    number of positions down the alphabet.

    Parameters
    -----------
    text : text that is going to be encrypted
    shift : the number of positions down the alphabet to be used for encryption
    encrypt : takes in boolean values, decides whether to encrypt text or not

    Returns
    --------
    Newly encrypted text.

    Examples
    ---------
    >>>> import pandas as pd
    >>>> cipher('Test', 5)
    'Yjxy'

    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text