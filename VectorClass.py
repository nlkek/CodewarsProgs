class Vector:
    def __init__(self, lst):
        self.lst = lst
        
    def __str__(self):
        return str(tuple(self.lst)).replace(' ','')
        
    def equals(self, vector):
        if self.lst == vector.lst:
            return True
        return False
        
    def add(self, vector):
        return Vector(list(map(sum, zip(self.lst, vector.lst))))
        
    def subtract(self, vector):
        return Vector(list(map(lambda x: x[0] - x[1], zip(self.lst, vector.lst))))
        
    def dot(self, vector):
        return sum(map(lambda x: x[0] * x[1], zip(self.lst, vector.lst)))
        
    def norm(self):
        return self.dot(self) ** 0.5
        
        """
        Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return Vector([4, 6, 8])
a.subtract(b) # should return Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals method, to check that two vectors that have the same components are equal
Note: the test cases will utilize the user-provided equals method.
"""
