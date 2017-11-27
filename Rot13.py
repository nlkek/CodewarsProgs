import string
from codecs import encode as _dont_use_this_


def rot13(message):
    res = ''
    key = 'abcdefghijklmnopqrstuvwxyz'
    key_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in message:
        if i not in key and i not in key_upper:
            res+=i
        elif i in key_upper:
            print(i)
            res+=key_upper[(key_upper.index(i)+13)%26]
        else:
            res+=key[(key.index(i)+13)%26]
    return res
    
    """
    ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.
"""
