def func(original):
    return ['x' if not isinstance(i, list) else func(i) for i in original]
    
    
def same_structure_as(original,other): 
    if type(original) != type(other):
        return False
    if func(original) == func(other):
        return True
    return False
    
    """
    Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structure as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""
