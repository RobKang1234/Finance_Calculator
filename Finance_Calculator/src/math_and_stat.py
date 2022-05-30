"""This file provides fundamental mathematical and statastical calculations 


"""
import math
class UnexpectedError(Exception):
    pass
class InputError(Exception):
    pass
class math_formula():
    def arithmetic_mean(self):
        """Calculate arithmetic mean of a list
        """
        suming = 0
        for item in self:
            suming += item
        return suming/len(self)
            
class create_matrix():
    def transform_matrix(self=True, a = [['0']]):
        """Transfer matrix a of form [['0']] to [[0]]
        """
        return [[0]]
    
    def zero_matrix(self=True, cols=1, rows=1):
        """Return a zero matrix with dimension rows x cols
        
        """
        matrix = [[]]
        colsE = []
        i = 0
        while(i < cols):
            colsE.append(0)
        k = 0
        while(k < rows):
            matrix.append(colsE)
       
    def identity_matrix(self=True, cols=1, rows=1):
        """Return a cols x rows identity matrix 
        cols must be equal to rows
        """
        if(cols != rows):
            raise ValueError("Not a square matrix!")
        else:
            
            matrix = create_matrix.zero_matrix(True, cols, rows)
            i = 0
            while(i < cols):
                matrix[i][i] = 1
                i = i + 1
            return matrix
        
    def Jmatrix(self=True, cols=1, rows=1):
        """Return a Jmatrix of given rows and cols
        
        """
        Jmatrix = [[]]
        colsE = []
        k = 0
        while(k < cols):
            colsE.append(1)
        i=0
        while (i <= rows):
            Jmatrix.append(colsE)
        return Jmatrix
    
    def reduce_matrix(self=True, a=[[0]], col_to_elin=0, row_to_elin=0):
        """Return a matrix given a with col_to_elin removed and row_to_elin removed
        
        >>> a = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        >>> b = reduce_matrix(a=a, col_to_elin=0, row_to_elin=0)
        >>> ans = [
            [5, 6]
            [8, 9]
        ]
        >>> b == Answer
        True
        """
        if col_to_elin >= len(a[0]):
            raise InputError("Index starts at 0. Index out of range")
        if row_to_elin >= len(a):
            raise InputError("Index starts at 0. Index out of range")
        lists = []
        rows = []
        empty_matrix = []
        for i in range(len(a)):
            for j in range(len(a[0])):
                if i != row_to_elin and j != col_to_elin:
                    lists.append(a[i][j])
        
        m = int(math.sqrt(len(lists)))
       
        n = 0
        k = 0
        l = 0
        o = 2
        t = 1
        while n < m:
            for c in range(k,m+l):
                rows.append(lists[c])
                k = k + 1
            l = k
           
            empty_matrix.append(rows)
            rows = []
            if t%2 == 0:
                k = k + m - o
            else:
                k = k + m - 1 - o 
            n = n + 1
            o = o + 1
            t = t + 1
        return empty_matrix
                
    
    def random_matrix(self=True, cols=1, rows=1, ranges=[1,10], decimals=0):
        """Randomly generate a matrix of size rows x cols with random
        number range in ranges and leave decimals number of decimal
        
        """
        
            
            
        
class check_valid_inputs():
    """Check if all the inputs of the  classes of functions 
    are both mathematically and stattistically valid 
    
            ==========          ===============
            Functions           Descriptions
            ==========          ===============
            isValidMatrix       Return True iff the input matrix a is valid
            isSquareMatrix      Return True iff a is a square matrix 
        
    """
    def isValidMatrix(self=True, a=[[0]]):
        """Return True iff the input matrix a is valid
        (i.e. Matrix have same number of rows for each colmun)
        
        - Please enter [['0']] for 1x1 0 matrix
        """
        #Wrong input
        if a == [[0]]:
            raise InputError("Unexpected input [[0]], Do you mean [['0']] for 1x1 zero matrix")
        m = len(a)
        len_list = []
        for i in range(m):
            len_list.append(len(a[i]))
        avg = math_formula.arithmetic_mean(len_list)
        if avg != len_list[0]:
            raise InputError("Invalid matrix form")
        return True
        
    def isSquareMatrix(self=True, a=[[0]]):
        """Return True iff a is a square matrix 
        
        Assume all input matrix are valid
        """
        m = len(a)
        n = len(a[0])
        if m != n:
            return False
        return True
         
def matrixDet(a):
    """This function calculate and return the determint of matrix a
    using a recursive method.
    """
    # Check valid inputs
    #check_valid_inputs.isValidMatrix(True, a)
    #if check_valid_inputs.isSquareMatrix(True, a) == False:
    #    raise InputError("Input matrix is not square")
    
    #base case
    if len(a)==2 and len(a[0])==2:
        det = a[0][0]*a[1][1]-a[0][1]*a[1][0]
        return det
    else:
        sol = 0
        for i in range(len(a)):
            print(create_matrix.reduce_matrix(True, a, 0, i))
            fac = (-1)**(0+i)*a[0][i]+matrixDet(create_matrix.reduce_matrix(True, a, 0, i))
        sol = sol + fac
        return sol
            
        
    
    
    
class matrix_functions():
    """Check the type of Matrix - square, non- square etc. 
    Have functions of:
    
        ==========          ===============
        Functions           Descriptions
        ==========          ===============
        matrix_type         Return type of the matrix - either square or non-square
        col_rows            Return the number of cols and rows of a matrix (cols, rows) in a tuple
        ifInverse           Return a true if it is a inverse Matrix 
        ifSingular          Return a Matrix if it is singular
        
    """
    def matrix_type(self=True, a = [[0]]):
        """Return type of the matrix - either square or non-square
        
        Pre-condition: Input matrix is valid
        
        Docstrings
        """
        col_a = len(a)
        num_element = len(a[0])
        if (col_a == num_element):
            return "Square"
        return "Non-Square"
    
    def col_rows(self=True, a = [[0]]):
        """Return the number of cols and rows of a matrix (cols, rows) in a tuple
        
        Pre-condition: Input matrix is valid
        
        Docstrings
        """
        cols = len(a)
        rows = len(a[0])
        return (cols, rows)
    
    def ifInverse(self=True, a = [[0]]):
        """Return a true if it is a inverse Matrix
        
        Pre-condition: Input matrix is valid
        """
        
        
        

        

class matrix_calculation():
    """Under this class, providing calculators for:
    
            - Matrix Addition
            - Matrix Substraction
            - Matrix Multiplication
            - Matrix Inversion
            - Matrix Determint 
    """
    
    def matrix_addition(self=True, a=[[0]], b=[[0]]):
        """Return an added matrix between a and b such that a+b
        
        >>> a = [[1, 2, 3],
                 [2, 5, 7],
                 [9, 2, 6]]
        >>> b = [[3, 4, 0],
                 [1, 9, 7],
                 [12, 4, 3]]
        >>> c = [[4, 6, 3],
                 [3, 14, 14],
                 [21, 16, 20]]
        >>> a + b == c
        True
        """
        #Check inputs
        if (a == [[0]] and b == [[0]]):
            raise ValueError("Input not valid by default. Please enter inputs for two matrices\n")

        #Check if a and b have equal cols
        num_col_a = len(a)
        num_col_b = len(b)
        if (num_col_a != num_col_b):
            raise ValueError("Matrix A must have the same number of columns. \
                             Currently, Matrix A has %d columns and Matrix B has %d columns" %(num_col_a, num_col_b))
        
        #Check if a or b is valid matrix. (i.e. Each row has the same number of elements)
        for i in range(len(a)):
            for j in range(1,len(a)):
                if(len(a[i])!=len(b[j])):
                    raise ValueError("Invalid Matrix From, each row of the matrix \
                                     should have the same number of elements")
        
        #Check if 