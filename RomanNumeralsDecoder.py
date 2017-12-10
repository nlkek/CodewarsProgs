def solution(s):
    res = 0
    i = 0
    s = list(s[::-1])
    d = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
    print(s)
    while len(s) > 1:
        if d[s[i]] > d[s[i+1]]:
            tmp = ''
            tmp = s[i+1] + s[i]
            res += d[''.join(tmp)]
            s.pop(i)
            s.pop(i)
        else:
            res += d[s[i]]
            s.pop(i)
    if s:
        res += d[s[0]]
    return res
    
    
"""
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

solution('XXI') # should return 21
"""
