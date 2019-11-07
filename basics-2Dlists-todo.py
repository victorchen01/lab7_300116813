import random

# programming exercise  1

def make_matrix_random(a,b, x, y):
     '''(int,int,int)->2D list
     Returns a 2D list representing a matrix with a rows and b columns
     filled with random integers >=x and <=y
     Precondition: a,b positive and x <=y
     '''

     m = []
     for i in range(a):
          row = []
          for j in range(b):
               row.append(random.randint(x,y))
          m.append(row)
     return m

# programming exercise  2
def sum_above_diagonal(m):
     '''(2D list)->number
     Returns the sum of the elements of the matarix m that are on or about the diagonal of m
     (for clarification see the slide entitled: Details about Prog Ex 2)
     Precondition: m is a square matrix filled with numbers

     >>> sum_above_diagonal([[1,2],[10,20]] )
     23
     '''

     sumAD = 0

     for i in range(len(m)):
         for j in range(len(m)):
             if(j >= i):
                 sumAD += m[i][j]

     return sumAD

# programming exercise  3
def max_over_all_even_cols(m):
     '''(2D list)->number
     Returns the maximum element among all the numbers that are in even columns of m
     i.e the maximum element amoung all elements in 0th, 2th, 4th etc. column
     Precondition: m is a matrix filled with numbers with at least 1 row and 1 column

     >>> max_over_all_even_cols([1,1,1,1,1,1,1],[1,10,3,20,12,6,0] )
     12
     '''

     maxNum = 0

     for i in range(len(m)):
         for j in range(0,len(m[i]),2):
             if(m[i][j] > maxNum):
                 maxNum = m[i][j]

     return maxNum

#programming exercise  4
def max_each_row(m):
     '''(2D list)->list
     Returns a list where in position p of the list is the max number among all the numebrs of p-th row of m
     Precondition: m is a matrix filled with numbers

     >>> max_each_row([[1,2],[200,0],[3,3],[-10,-20]])
     [2, 200, 3, -10]
     '''
     maxLst = []

     for i in range(len(m)):
         maxNum = m[i][0]
         for j in range(len(m[i])):
             if(m[i][j] > maxNum):
                 maxNum = m[i][j]
         maxLst.append(maxNum)

     return maxLst

# programming exercise  5
def index_of_max_sum_row(m):
     '''(2D list)->int
     Returns the index of a row that has the largest sum of all the rows
     Precondition: m is a matrix filled with numbers
     >>> index_of_max_sum_row([[100,100], [-100,0], [200,30], [1,2]])
     2
     >>> index_of_max_sum_row([[100,100], [-100,0], [200,30], [10000,2]])
     3
     '''

     sumsR = []

     for i in range(len(m)):
         rowSum = 0
         for j in range(len(m[i])):
             rowSum += m[i][j]
         sumsR.append(rowSum)

     maxSums = sumsR[0]

     for i in range(len(sumsR)):
         if(sumsR[i] > maxSums):
             maxSums = sumsR[i]

     return sumsR.index(maxSums)

print(make_matrix_random(5,5, 1, 12))
print(sum_above_diagonal([[1,2],[10,20]] ))
m = ([1,1,1,1,1,1,1],[1,10,3,20,12,6,0])
print(max_over_all_even_cols(m))
print(max_each_row([[1,2],[200,0],[3,3],[-10,-20]]))
print(index_of_max_sum_row([[100,100], [-100,0], [200,30], [1,2]]))
