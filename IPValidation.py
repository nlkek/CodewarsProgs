def is_valid_IP(s):
    i = 0
    lst = s.split('.')
    if len(lst) != 4:
        return False
    for ip in lst:
        if ip.isdigit() and len(ip) == 1 and int(ip) in range(0,10):
            i+=1       
        elif ip.isdigit() and int(ip) in range(0, 256) and ip[0]!='0':
            i+=1
    return i == 4
    
    """
    Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0..255 (included).

Input to the function is guaranteed to be a single string.

Examples

// valid inputs:
1.2.3.4
123.45.67.89

// invalid inputs:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Note: leading zeros (e.g. 01.02.03.04) are considered not valid in this kata!
"""
