from fractions import Fraction

def op(a,b,op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
        
def calc(stri):
    ops = '+-*/'
    stack = []
    s = stri.split(' ')
    for c in s:
        if c in ops:
            a = stack.pop()
            b = stack.pop()
            stack.append(op(b, a, c))
        elif c.isdigit():
            stack.append(int(c))
        else:
            stack.append(float(c))
    num = stack[0]
    if type(num) == int:
        return num
    return float(Fraction(num).limit_denominator())


class Calculator(object):
    def evaluate(self, stri):
        s = stri.split(' ')
        sout = ''
        ops = '+-*/'
        prior = {'+':1,'-':1,'*':2,'/':2,'(':0,')':0}
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                while stack[len(stack)-1] != '(':
                    sout+=stack.pop() + ' '
                stack.pop()
            elif c in ops:
                if not stack:
                    stack.append(c)
                else:
                    while prior[c] <= prior[stack[len(stack) - 1]]:
                        sout+=stack.pop() + ' '
                        if not stack:
                            break
                    stack.append(c)
            
            elif c.isdigit():
                sout+=c + ' '
            else:
                sout+=c + ' '
              
        while stack:
            sout += stack.pop() + ' '
        sout = sout.rstrip()
        return calc(sout)
      
        #Create a simple calculator that given a string of operators (+ - * and /) and numbers separated by spaces returns the value of that expression
        #Example:
        #Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
        #Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.
        
