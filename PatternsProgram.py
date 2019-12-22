def starPyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print("\r")
n=5
starPyramid(n)
#####################################
""" output:
*
**
***
****
*****
"""
#####################################
def starPyramid2(n):

    for i in range(0,n):
        for j in range(0,n-1):
            print(end=" ")

        n =n -1
        for j in range(0,i+1):
            print("*",end="")
        print("\r")
n=5
starPyramid2(n)
######################################
""" output
    *
   **
  ***
 ****
*****
"""
######################################
def starTriangle(n):
    k = (2*n) - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
n=5
starTriangle(5)
#########################################
"""
output
       * 
      * * 
     * * * 
    * * * * 
   * * * * * 
"""
##########################################
def reverseHalfPyramid(n):
    for i in range(5,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print("\r")
n=5
reverseHalfPyramid(n)
######################################
"""
* * * * * 
* * * * 
* * * 
* * 
* 
"""
####################################
