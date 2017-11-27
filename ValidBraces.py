def validBraces(string):
    stack = []
    open_braces, close_braces = '([{', ')]}'
    for s in string:
        if s in open_braces:
            stack.append(s)
        elif s in close_braces:
            if not len(stack):
                return False
            else:
                c = stack.pop()
                if close_braces.index(s) != open_braces.index(c):
                    return False
    if not len(stack):
        return True
    return False
    
    """
    Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?

A string of braces is considered valid if all braces are matched with the correct brace.

Examples

"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""
