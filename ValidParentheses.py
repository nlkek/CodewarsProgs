def valid_parentheses(string):
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
    Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""
