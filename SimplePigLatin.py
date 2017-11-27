def pig_it(text):
    res = ''
    lst = text.split(' ')
    for word in lst:
        if word.isalnum():
            res += word[1:] + word[0] + 'ay '
        else:
            res += word
    return res.rstrip()
    
    """
    Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldWay !
"""
