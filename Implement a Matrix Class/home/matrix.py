import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):
    """
    Math matrix class
    Attributes:
        g: The data grid
        h: The matrix height
        w: The matrix width
    Important note:
    Determinant and inversion only supported up to a size of 2x2.
    """
    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise (ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise (NotImplementedError, "Calculating determinant not implemented for matrices larger than 2x2.")
        # TODO - your code here
        if self.h == 1:
            return self.g[0][0]
        if self.h == 2:
            return self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
        return None

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        # TODO - your code here
        if not self.is_square():
            raise (ValueError, "Cannot calculate the trace of a non-square matrix.")
        trace = 0.0
        for i in range(self.h):
            trace += self[i][i]
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise (ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise (NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        # TODO - your code here
        if self.determinant() == 0.:
            raise ValueError('The matrix has no inverse')
        if self.h == 1:
            inverse = [[1 / self.determinant()]]
        if self.h == 2:
            inverse = [[self.g[1][1] * 1 / self.determinant(), -self.g[0][1] * 1 / self.determinant()],
                       [-self.g[1][0] * 1 / self.determinant(), self.g[0][0] * 1 / self.determinant()]]
        return Matrix(inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix = zeroes(self.w, self.h)       
        for i in range(self.h):
            for j in range(self.w):
                matrix[j][i] = self.g[i][j]
        return matrix

    def is_square(self):
        """
        Returns if width matches height
        :return: True if the matrix is square
        """
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self, idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.
        Example:
        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]
        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self, other):
        """
        Defines the behavior of the + operator
        other: The matrix to be added
        """
        if self.h != other.h or self.w != other.w:
            raise (ValueError, "Matrices can only be added if the dimensions are the same")
        # TODO - your code here
        matrix = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                matrix[i][j] = self.g[i][j] + other.g[i][j]
        return matrix
    
    
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)
        Example:
        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        # TODO - your code here
        matrix = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                 matrix[i][j] = self.g[i][j]*-1.0
        return matrix
    
    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        other: The matrix to be subtracted
        """
        if self.h != other.h or self.w != other.w:
            raise (ValueError, "Matrices can only be subtracted if the dimensions are the same")
        # TODO - your code here
        matrix = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                matrix[i][j] = self.g[i][j]-other.g[i][j]
        return matrix

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        other: The matrix to be multiplied with.
        """
        if self.w != other.h:
            raise (ValueError, "Matrices can only be multiplied if the own row count matches the other's column count")
        # TODO - your code here
        matrix = zeroes(self.h, other.w)
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                    matrix[i][j] += self.g[i][k] * other.g[k][j]
        return matrix

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.
        Example:
        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #   
            # TODO - your code here
            matrix = self
            for i in range(self.h):
                for j in range(self.w):
                    matrix[i][j] *= other
            return matrix