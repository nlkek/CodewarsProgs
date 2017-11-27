res = []
def rotate_180(m):
    rotated = zip(*m[::-1])
    return [list(i) for i in list(zip(*list(rotated)[::-1]))]

def walk(m):
    if m == [[]]:
        return
    if len(m) == 1:
        res.append(m[0][0])
        return 
    for i in m[0]:
        res.append(i)
    m.pop(0)
    for i in m:
        res.append(i.pop(len(i)-1))
    walk(list(rotate_180(m)))
    
def snail(array):
    global res
    res = []
    walk(array)
    return res
    
    """
    Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:



NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as [[]]
"""
