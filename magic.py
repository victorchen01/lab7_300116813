def is_square(m):
     '''2d-list => bool
     Return True if m is a square matrix, otherwise return False
     (Matrix is square if it has the same number of rows and columns'''
     for i in range(len(m)):
          if len(m[i]) != len(m):
               return False
     return True


def magic(m):
     '''2D list->bool
     Returns True if m forms a magic square
     Precondition: m is a matrix with at least 2 rows and 2 columns '''

     # this tests the condition that is implied by the definition
     # i.e. that m has to be a square matrix
     if(not(is_square(m))): # if matrix is not square
          return False      # return False

     # TEST CONDITION 1
     testLst = []
     for i in range(len(m)):
         for j in range(len(m)):
            if(m[i].count(m[i][j]) > 1):
                return False

     # TEST CONDITION 2

     xsumLst = []
     ysumLst = []
     dsumLst = []

     for i in range(len(m)):
         sumX = 0
         for j in range(len(m)):
             sumX += m[i][j]
         xsumLst.append(sumX)

     for i in range(len(m)):
         sumY = 0
         for j in range(len(m)):
             sumY += m[j][i]
         ysumLst.append(sumY)

     sumD = 0

     for i in range(len(m)):
         sumD += m[i][i]

     dsumLst.append(sumD)
     sumD = 0

     for i in range(len(m)):
         sumD += m[i][len(m)-i-1]

     dsumLst.append(sumD)

     if((xsumLst.count(xsumLst[0]) != len(xsumLst)) or (ysumLst.count(ysumLst[0]) != len(ysumLst)) or (dsumLst.count(dsumLst[0]) != 2)):
         return False
     elif(xsumLst[0] != ysumLst[0] or xsumLst[0] != dsumLst[0] or dsumLst[0] != ysumLst[0]):
         return False
     else:
         return True

# main
# TESTING OF magic functions

# this should print True

m0=[[2,7, 6],[9,5,1],[4,3,8]]
print(magic(m0))

# this should print True
m1 = [[16,3,2,13], [5,10,11,8],[9,6,7,12], [4,15,14,1]]
print(magic(m1))

# this should print False. Why? Which condition imposed on magic squares is not true for m3
m2 = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(magic(m2))

#this should print False. Why? Which condition imposed on magic squares is not true for m3
m3 =  [[1,1],[1,1]]
print(magic(m3))

# #this should print False. Why? Which condition imposed on magic squares is not
m3 =  [[1,1],[1,1],[1,2]]
print(magic(m3))
