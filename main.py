# Program1

# *
# **
# ***
# ****
# *****

# n = int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print("*"*i)

# ------------------------------------------------

# Program2

# *
# **
# ***
# ****
# *****

# n = int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end = "")
#     print()
# -------------------------------------------------

# Program3

# *
# ***
# *****
# *******
# *********

# n = int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#      for j in range(2*(i)-1):
#          print("*", end = "")
#      print()
# -------------------------------------------------


# Program4

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end = "")
#     for k in range(i+1):
#         print("* ",end = "")
#     print()
# -------------------------------------------------


# Program5

# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n =int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i):
#         print(" ",end = "")
#     for j in range(n-i):
#         print("*",end =" ")
#     print()

# -------------------------------------------------


# Program6

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end = "")
#     for j in range(n-i-1):
#         print("*",end =" ")
#     print()
#

# -------------------------------------------------


# Program7

# *****
# ****
# ***
# **
# *

# n = int(input("Enter the number of rows: "))
# for i in range(n,0,-1):
#     print("*"*i)

# -------------------------------------------------

#Program8

# *****
# ****
# ***
# **
# *


# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(n-i):
#         print("*", end = "")
#     print()

# --------------------------------------------------------------------------------
# --------------ALPHABETS-----------(ABCDEFGHIJKLMNOPQRSTUVWXYZ)-------------------------------

# Program 9  A
# for row in range(7):
#     for col in range(5):
#         if ((col == 0 or col == 4) and row !=0) or ((row ==0 or row == 3) and (col >0 and col<4)):
#             print("#",end = " ")
#         else:
#             print(" ",end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 10 B
# for row in range(7):
#     for col in range(5):
#         if ((row%3== 0) and col != 4) or ((col==0 or col== 4) and row%3!=0):
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 11 C
# for row in range(7):
#     for col in range(5):
#         if row == 0 or row == 6 or col == 0:
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 12 D
# for row in range(7):
#     for col in range(5):
#        if (col == 0) or (col == 4 and (row !=0 and row != 6)) or ((row == 0 or row == 6) and (col>0 and col<4)):
#            print("*",end = "")
#        else:
#            print(end=" ")
#     print()
# --------------------------------------------------------------------------------

# Program13 E
# for row in range(7):
#     for col in range(5):
#         if col == 0 or row%3==0:
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program13 F
# for row in range(7):
#     for col in range(5):
#         if col == 0 or row==0 or row == 3:
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()

# Program 14 G
# --------------------------------------------------------------------------------

# for row in range(7):
#     for col in range(6):
#         if col == 0 or (col == 4 and (row != 1 and row != 2)) or ((row ==0 or row == 6) and (col >0 and col <4)) or (row==3 and (col ==3 or col==5)):
#             print("*",end =" ")
#         else:
#             print(" ",end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 15 H
# for row in range(7):
#     for col in range(5):
#         if col == 0 or col == 4 or (row == 3 and (col >0 and col <4)):
#             print("*",end = " ")
#         else:
#             print(" ",end =" ")
#     print()
# --------------------------------------------------------------------------------

# Program 16 I
# for row in range(7):
#     for col in range(5):
#         if ((row == 0) or (row == 6) and col != 2) or (col == 2):
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 17 J

# for row in range(5):
#     for col in range(5):
#         if (col == 2) or (row == 0) or (row == 4 and col <3):
#             print("*",end = " ")
#         else:
#             print(" ",end =" ")
#     print()

# --------------------------------------------------------------------------------

# program 18 K
# for row in range(7):
#     for col in range(5):
#         if col == 0 or (row + col == 4) or (row - col == 2):
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 19 L
# for i in range(5):
#     for j in range(5):
#         if i == 4 or j == 0:
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 16 M

# for row in range(7):
#     for col in range(7):
#         if col == 0 or col == 6 or ((row == col)and col <4) or (row == 2 and col == 4) or ((row == 1 ) and (col==5)):
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()

# --------------------------------------------------------------------------------

# Program 17 N
# for row in range(7):
#     for col in range(7):
#         if col == 0 or col == 6 or row == col:
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 18 O
# for row in range(7):
#     for col in range(5):
#         if ((row == 0 or row == 6) and (col > 0 and col < 4)) or (col == 0 or col == 4) and (row != 0 and row != 6):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 19 P
# for row in range(7):
#     for col in range(5):
#         if col == 0 or ((row == 0 or row == 3) and col !=4) or (row == 1 and col==4) or (row == 2 and col == 4):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 20 Q
# for row in range(8):
#     for col in range(5):
#         if ((col == 0 or col == 4) and (row > 0 and row < 6)) or ((row == 0 or row== 6) and (col >0 and col < 4)) or (row == 5 and col == 1) or (row == 7 and col == 3):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()
# --------------------------------------------------------------------------------

#Program 21 R
# for row in range(7):
#     for col in range(5):
#         if col == 0 or ((row != 0 and row != 3) and col==4) or ((row == 0 or row == 3) and (col >0 and col < 4)):
#             print("*",end =" ")
#         else:
#             print(" ", end = " ")
#     print()
# --------------------------------------------------------------------------------

#Program 25 S
# for row in range(7):
#     for col in range(5):
#         if ((row == 0 or row == 3 or row == 6) and (col>0and col < 4)) or (row == 1 and col==0 ) or (row == 2 and col== 0) or (row == 5 and col == 4) or (row == 4 and col == 4):
#             print("*",end =" ")
#         else:
#             print(" ", end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 26 T
# for row in range(7):
#     for col in range(7):
#         if row == 0 or col ==3:
#             print("*", end = " ")
#         else:
#             print(" ",end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 27 U
# for row in range(7):
#     for col in range(5):
#         if ((col == 0 or col== 4) and (row != 6)) or (row == 6 and (col>0 and col <4)):
#             print("*",end =" ")
#         else:
#             print(" ", end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 28 V
# for row in range(4):
#     for col in range(7):
#         if row ==col or col + row == 6:
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 29 W
# for row in range(4):
#     for col in range(7):
#         if (col == 0) or (col == 6) or (row +col == 3) or (col - row == 3):
#             print("*",end =" ")
#         else:
#             print(" ", end = " ")
#     print()
# --------------------------------------------------------------------------------

# Program 30 X
# for row in range(5):
#     for col in range(5):
#         if (row ==col ) or (row +col == 4):
#             print("*",end =" ")
#         else:
#             print(" ",end = " ")
#     print()
# --------------------------------------------------------------------------------

#  Program 31 Y
# for row in range(5):
#     for col in range(5):
#         if (col == 2 and row>1) or (row == col and col <2) or (row == 1 and col ==3) or (row == 0 and col ==4) :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# --------------------------------------------------------------------------------

# program 32

# * * * * *
#   *     *
#     *   *
#       * *
#         *

# n = int(input("Enter the number of rows: "))
# for row in range(n):
#     for col in range(n):
#         if row == 0 or col == n-1 or (row == col):
#
#
#             print("*", end = " ")
#         else:
#             print(" ",end = " ")
#     print()

# --------------------------------------------------------------------------------

# Program 33 Z
# for row in range(6):
#     for col in range(6):
#         if row == 0 or row == 5 or (row +col == 5):
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()

# ----------------------END OF ALPHABETS----------------------------------------------------------


# Program 34

# 1
# 2   3
# 4   5   6
# 7   8   9   10
# 11  12  13  14  15
#
# rows = int(input("Enter the number of rows: "))
# k = 1
# for i in range(rows):
#     for j in range(i+1):
#         print(format(k,"<3"),end = " ")
#         k = k +1
#     print()


# --------------------------------------------------------------------------------


# Program 36

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# num =int(input("Enter the number of number: "))
#
# for i in range(num):
#     for j in range(num-i):
#         print(j+1,end = " ")
#     print()

# --------------------------------------------------------------------------------

# Program 37

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# num = int(input("Enter the number : "))

# for i in range(num):
#     for j in range(num-i,0,-1):
#         print(num-i,end = " ")
#     print()

# program 38
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(i+1):
#         print("*",end = " ")
#     print()
# --------------------------------------------------------------------------------


# Program 39

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         print("*",end =" ")
#     print()

# --------------------------------------------------------------------------------

# Program 40 Hollow Diamond Shape

#     *
#   *   *
# *       *
#   *   *
#     *

# for row in range(5):
#     for col in range(5):
#         if (row+col == 2) or (row - col ==2) or (col - row == 2) or (row + col == 6):
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()
# --------------------------------------------------------------------------------

# program 37

#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *
#
# n = int(input("Enter the number of rows: "))
# for row in range(1,n+1):
#     for col in range(1,2*n):
#         if (row + col == n+1) or (row == n) or (col - row == n-1):
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()

# --------------------------------------------------------------------------------


# Program 38

#         *
#       *   *
#     *       *
#   *           *
# *   *   *   *   *

# n = int(input("Enter the number of rows: "))
# k = 2
# for row in range(1,n+1):
#     for col in range(1,2*n):
#         if (row +col == n+1) or (col - row == n-1):
#             print("*",end = " ")
#         elif row == n and col != k:
#             print("*", end=" ")
#             k =k+2
#         else:
#             print(" ", end = " ")
#     print()

# --------------------------------------------------------------------------------


# Program 39

#   * *   * *
# *     *     *
# *           *
#   *       *
#     *   *
#       *

# for row in range(6):
#     for col in range(7):
#         if (row == 0 and col%3!= 0) or (row ==1 and col %3 == 0) or (row - col == 2) or (row +col == 8):
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()

# --------------------------------------------------------------------------------
# Program 40
#  1	 2	 3	 4	5
# 16	17	18	19	6
# 15	24	25	20	7
# 14	23	22	21	8
# 13	12	11	10	9


# num = int(input("Enter the number of rows: "))
# nested_list = [[0 for x in range(num)] for y in range(num)]
# n = 1
# low = 0
# high = num-1
# count = int((num+1)/2)
# for i in range(count):
#     for j in range(low,high+1):
#         nested_list[i][j] = n
#         n= n+1
#     for j in range(low+1,high +1):
#         nested_list[j][high]= n
#         n+=1
#     for j in range(high-1, low-1,-1):
#         nested_list[high][j] = n
#         n+=1
#     for j in range(high-1,low,-1):
#         nested_list[j][low] = n
#         n+= 1
#     low +=1
#     high -=1


# for i in range(num):
#     for j in range(num):
#         print(nested_list[i][j],end ="\t")
#     print()
# ------------------------------------------------------------------------
# Program 42

#     1
#    212
#   32123
#  4321234
# 543212345
#
#
# num = int(input("Enter the number of rows: "))
# for i in range(1,num+1):
#     for j in range(1,num -i+1):
#         print(" ", end ="")
#     for k in range(i,0,-1):
#         print(k,end = "")
#     for j in range(2,i+1):
#         print(j,end = "")
#     print()

# ------------------------------------------------------------------------

# Program 45
# num = int(input("Enter the number of cols: "))
# n = num//2
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         print("* ",end ="")
#
#     if num%2==0:
#         for j in range(2*(n - i - 1)):
#             print(" ", end="")
#     else:
#         for j in range(2*(n-i-1)+1):
#             print(" ", end = "")
#     for j in range(i + 1):
#             print("* ", end="")
#
#     print()
#
# for i in range(num,0,-1):
#     for j in range(num-i):
#         print(" ",end ="")
#
#     for j in range(i, 0,-1):
#         print("*",end =" ")
#     print()


# ----------------------------------------------------------------------------


#Program 46

#    *       *
#   * *     * *
#  * * *   * * *
# * * * * * * * *
# * * s m i t * *
# * * * * * * * *
#  * * * * * * *
#   * * * * * *
#    * * * * *
#     * * * *
#      * * *
#       * *
#        *





# num = int(input("Enter the number of cols: "))
# msg = input("Enter the name: ")
# l =len(msg)
# n = num//2
# for i in range(n):
#     print(" "*(n-i-1)+"* "*(i+1), end = "")
#     if num%2==0:
#         for j in range(2*(n - i - 1)):
#             print(" ", end="")
#     else:
#         for j in range(2*(n-i-1)+1):
#             print(" ", end = "")
#     for j in range(i + 1):
#             print("* ", end="")
#     print()
# if num%2 ==0:
#    if l%2 ==0:
#         print("* "*((num-l)//2)+ " ".join(msg)+ " *"*((num-l)//2))
#    else:
#        print("* " * ((num - l) // 2) + " ".join(msg) + " *" * (((num - l) // 2)+1))
# else:
#     if l % 2 == 0:
#         print("* " * ((num - l) // 2) + " ".join(msg) + " *" * (((num - l) // 2)+1))
#     else:
#         print("* " * ((num - l) // 2) + " ".join(msg) + " *" * (((num - l) // 2)))
#
# for i in range(num,0,-1):
#     print(" "*(num-i)+"* "*i)
# -------------------------------------------------


# Program 47

# 1
# 2    7
# 3    8    12
# 4    9    13   16
# 5    10   14   17   19
# 6    11   15   18   20   21

# num = int(input("Enter the number of rows:"))
# for i in range(num):
#     val = i+1
#     inc = num -1
#     for j in range(i+1):
#         print(format(val, "<4"),end = " ")
#         val = val + inc
#         inc = inc-1
#     print()

# -------------------------------------------------

# Program 48

# 1
# 2  9
# 3  8  10
# 4  7  11 14
# 5  6  12 13 15

# num = int(input("Enter the number of rows: "))
#
# for i in range(num):
#     for j in range(i+1):
#         x = 0
#         for k in range(j):
#             x = x+num-k
#         if j %2 == 0:
#             print(format(x+i-j+1,"<3"),end = "")
#         else:
#             print(format(format(x+num-i),"<3"),end = "")
#     print()


# -------------------------------------------------

# Program 49

# $ $ $ $ $
# $ $ $ $ $
# $ $ $ $ $
# $ $ $ $ $
# $ $ $ $ $

# num = int(input("Enter the number of rows: "))
# for i in range(num):
#
#     for j in range(num):
#         print(format("$","<2"), end = "")
#     print()

# ----------

# $
# $ $
# $ $ $
# $ $ $ $
# $ $ $ $ $

# num = int(input("Enter the number of rows: "))
# for i in range(num):
#
#     for j in range(i+1):
#         print(format("$","<2"), end = "")
#     print()

# --------------------OR---------------

# $
# $ $
# $ $ $
# $ $ $ $
# $ $ $ $ $

# num= int(input("Enter the number of rows: "))
# for i in range(1,num+1):
#     print("$"*i)

# -----------------------------------------------

#     *
#    **
#   ***
#  ****
# *****

# num= int(input("Enter the number of rows: "))
# for i in range(num,0,-1):
#     print(" "*(i-1) + "$"*(num-i+1))

# ------------------------------------------------

#     *
#    * *
#   * * *
#  * * * *
# * * * * *


# num= int(input("Enter the number of rows: "))
# for i in range(1,num+1):
#     print(" "*(num-i)+ "* "*i)






# -------------------------------------------------

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# num= int(input("Enter the number of rows: "))
# for i in range(1,num+1):
#     print(" "*(num-i)+ "* "*i)
# for j in range(num-1,0, -1):
#     print(" "*(num-j)+"* "*(j))

# --------------------------------------------------
# * * * *
#  * * *
#   * *
#    *

# num= int(input("Enter the number of rows: "))
# for j in range(num,0, -1):
#     print(" "*(num-j)+"* "*(j))



# ----------------------------------------------------


# * * * * *
# * * * *
# * * *
# * *
# *

# num= int(input("Enter the number of rows: "))
# for j in range(num,0, -1):
#     print("* "*(j))

# ----------------------------------------------------


# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# num= int(input("Enter the number of rows: "))
# for j in range(num,0, -1):
#     print("  "*(num-j)+"* "*(j))


# ----------------------------------------------------
# Program 52

#     *
#    *A*
#   *A*A*
#  *A*A*A*
# *A*A*A*A*

# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     count = 0
#     for j in range(num-i-1):
#         print(" ",end = "")
#     for k in range(i+1):
#         print("*",end = "")
#         if count <i:
#                 print("A",end = "")
#                 count=count+1
#     print()

# ----------------------------------------------------

# Program 53


# 15
# 14  10
# 13  9   6
# 12  8   5   3
# 11  7   4   2   1

# num =int(input("Enter the number of rows: "))
#
# # To get the starting number:
#
# sum = 0
# for i in range(num,0,-1):
#     sum = sum +i
#
#
# # FinalProgram after getting the starting number
# for i in range(num):
#     val = sum -i
#     dec = num
#     for j in range(i+1):
#         print(format(val,"<4"),end ="")
#         dec =dec-1
#         val = val-dec
#     print()

# -------------------------------------------------

# Program 54

# 15
# 14  13
# 12  11  10
# 09  08  07  06
# 05  04  03  02  01

# num = int(input("Enter the number of rows: "))

# # To get the starting value
# sum = 0
# for i in range(num, 0, -1):
#     sum +=i
#
# # Actual program to print the numbers
# val =sum
# for i in range(num):
#     for j in range(i+1):
#         if val < 10:
#             print(format(f"0{val}", "<4"),end = "")
#         else:
#             print(format(val, "<4"), end="")
#         val = val-1
#     print()



# -------------------------------------------------
# Program 54

# 1   1
#  2 2
#   3
#  4 4
# 5   5


# num = input("Enter the odd length number: ")
#
# for i in range(len(num)):
#     for j in range(len(num)):
#         if (i == j) or ((i+j) == (len(num)-1)):
#             print(num[i], end="")
#         else:
#             print(" " ,end="")
#     print()
# ----------------------Another--------------------------

# 1   5
#  2 4
#   3
#  2 4
# 1   5

# num = input("Enter the odd length number: ")
#
# for i in range(len(num)):
#     for j in range(len(num)):
#         if (i == j) or ((i+j) == (len(num)-1)):
#             print(num[j], end="")
#         else:
#             print(" " ,end="")
#     print()


# ----------------------------------------------------

# Program 55

# 111
# 111 222
# 111 222 333
# 111 222 333 444
# 111 222 333 444 555


# num = int(input("Enter the number of rows: "))
#
# for i in range(num):
#
#     val = 111
#     for j in range(i+1):
#         print(format(val,"<4"),end = "")
#         val = val +111
#     print()

# ---------------------Another---------------------------

#                 111
#             222 111
#         333 222 111
#     444 333 222 111
# 555 444 333 222 111

# num = int(input("Enter the number of rows: "))


# k = 111
# for i in range(num):
#     val = (i+1)*k
#     for j in range(num-i-1):
#         print(format(" ","<4"), end="")
#     for j in range(i+1):
#         print(format(val, "<4"), end="")
#         val = val -k
#     print()
#

# -------------------Another-----------------------

#                 111
#             111 222
#         111 222 333
#     111 222 333 444
# 111 222 333 444 555


# num = int(input("Enter the number of rows: "))
#
# k = 111
# for i in range(num):
#     val = k
#     for j in range(num-i-1):
#         print(format(" ","<4"), end="")
#     for j in range(i+1):
#         print(format(val, "<4") , end="")
#         val = val+k
#     print()

# ----------------------------------------------------
# Program 56

# ********
# ***  ***
# **    **
# *      *
# *      *
# **    **
# ***  ***
# ********

# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num-i,0, -1):
#         print("*", end="" )
#     for j in range((2*i)):
#         print(" ",end ="")
#     for j in range(num-i,0,-1):
#         print("*", end = "")
#     print()
#
# for i in range(num):
#     for j in range(i+1):
#         print("*", end ="")
#     for j in range((2*(num-i))-2):
#         print(" ", end ="")
#     for j in range(i+1):
#         print("*", end = "")
#     print()

# ----------------------------------------------------
# Program 57
#          1
#        21 12
#      321   123
#    4321     1234
#      321   123
#        21 12
#          1


# n = int(input("Enter the number of rows: "))
# k = 1
# for i in range(n,0,-1):
#     val = (n-i)+1
#     for j in range((2*i)+1):
#         print(" ",end = "")
#     for j in range(n-i+1):
#         print(val,end ="")
#         val = val-k
#     val = val+k
#     if i<n:
#         for j in range(2*(n-i)-1):
#             print(" ",end = "")
#         for j in range(n-i+1):
#             print(val,end ="")
#             val = val +k
#     print()
# for i in range(n-1):
#     val = n-i-1
#     for j in range(2*i+n+1):
#         print(" ", end = "")
#     for j in range(n-i-1):
#         print(val,end ="")
#         val = val-k
#     val = val +k
#     if i<n-2:
#         for j in range(n-(2*(i+1))+1):
#             print(" ",end="")
#         for j in range(n-i-1):
#             print(val,end = "")
#             val = val +k
#     print()


# -------------------------------------------
#  Program 58
# 3   3   3   3   3
# 3   2   2   2   3
# 3   2   1   2   3
# 3   2   2   2   3
# 3   3   3   3   3


# num =int(input("Enter the number: "))
#
#
# nested_list = [[0 for i in range(2*num-1)] for j in range(2*num-1)]
# val = num
# low = 0
# high = len(nested_list)-1
#
#
# for i in range(num):
#     for j in range(low,high+1):
#         nested_list[low][j] = val
#     for j in range(low+1,high+1):
#         nested_list[j][high]= val
#     for j in range(low,high):
#         nested_list[high][j] = val
#     for j in range(low+1,high):
#        nested_list[j][low] = val
#     low = low +1
#     high= high-1
#     val = val-1
#
# for i in range(len(nested_list)):
#     for j in range(len(nested_list[i])):
#         print(format(nested_list[i][j],"<4"),end ="")
#     print()


# ------------------------------------------------------------
# Program 59

#                 1
#             1       1
#         1       2       1
#     1       3       3       1
# 1       4       6       4       1


# n = int(input(("Enter the number of rows: ")))
# nested_list = [[0 for i in range((2*n)-1)] for j in range(n)]
# centeral_index = len(nested_list)-1
#
# for row in range(len(nested_list)):
#     nested_list[row][centeral_index-row] = 1
#     nested_list[row][centeral_index+row] = 1
#
#     if row >0:
#             for j in range(0,(2*n)-3):
#                 nested_list[row][j+1]=nested_list[row-1][j]+nested_list[row-1][j+2]
#
#
# for i in range(len(nested_list)):
#     for j in range(len(nested_list[i])):
#         if nested_list[i][j]:
#             print(format(nested_list[i][j],"<4"),end ="")
#         else:
#             print(format(" ","<4"),end ="")
#     print()

# -------------------------------------------------------------------------------

# -----------------------------------Another -----------------------------------
#  Pascal's triangle


#               1
#             1   1
#           1   2   1
#         1   3   3   1
#       1   4   6   4   1
#     1   5   10  10  5   1
#   1   6   15  20  15  6   1
# 1   7   21  35  35  21  7   1


# n= int(input("Enter the row number:"))
# outer_list = []
# for i in range(n):
#     temp = []
#     for j in range(i+1):
#         if j==0 or j==i:
#             temp.append(1)
#         else:
#             temp.append(outer_list[i-1][j-1]+ outer_list[i-1][j])
#     outer_list.append(temp)
#
# # print(outer_list)
#
# for i in range(n):
#     for j in range(n-i-1):
#         print(format(" ","<2"),end = "")
#     for j in range(i+1):
#         print(format(outer_list[i][j],"<3"),end = " ")
#     print()


# -------------------------------------------------------------------
#  Program 65

# A
# B C
# C D E
# D E F G
# E F G H I



# alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
#              "N","O","P","Q","R","S","T","U","V","W","X","y","Z"]
#
#
# n = int(input("Enter the number of rows: "))
#
# for i in range(n):
#     for j in range(i+1):
#         print(alphabets[i+j],end =" ")
#     print()


# -------------------------------------------------------------------
#program 66

#             *
#           *   *
# * * * * * * * * * * * * *
#   *   *           *   *
#     *               *
#   *   *           *   *
# * * * * * * * * * * * * *
#           *   *
#             *

# n =int(input("Enter the number of rows(>5): "))
# col = 2*n-5
# mid = col//2
# for i in range(n):
#     for j in range(2*n-5):
#         if i==2 or i==n-3 or i+j == mid  or j-i==mid or i-j==2 or i+j==col+1:
#             print("*",end =" ")
#         else:
#             print(" ",end = " ")
#     print()

# -----------------------------------------------------------------
# Program 67


#         * 1
#       * * 2 3
#     * * * 3 4 5
#   * * * * 4 5 6 7
# * * * * * 5 6 7 8 9
# 5 4 3 2 1 1 3 5 7 9
#   5 4 3 2 3 5 7 9
#     5 4 3 5 7 9
#       5 4 7 9
#         5 9



# n =int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end =" ")
#     for j in range(i+1):
#         print("*",end = " ")
#     for j in range(i+1):
#         print(i+j+1,end = " ")
#     print()
#
# for i in range(n):
#     for j in range(i):
#         print(" ",end = " ")
#     for j in range(n-i):
#         print(n-j, end = " ")
#     for j in range(n-i):
#         print(2*(i+j)+1,end = " ")
#     print()

# -------------------------------------------------------------------
# Program 68 (Using Recursion)
#
# # *
# # * *
# # * * *
# # * * * *
# # * * * * *
#
#
# def print_right_star(num):
#     if num==0:
#         return
#     else:
#         print_right_star(num-1)
#         print("* "*num)
#
# num = int(input("Enter the number of rows:"))
# print_right_star(num)

# --------------------------------------------------------------------------

#  Program 69

# P
# yy
# ttt
# hhhh
# ooooo
# nnnnnn

# word ="Python"
#
# for i in range(len(word)):
#     for j in range(i+1):
#         print(word[i],end ="")
#     print()

# -------------------------------------------------------------------
#  Program 70

# P
# Py
# Pyt
# Pyth
# Pytho
# Python

# word = input("Enter the word: ")
# for i in range(len(word)):
#     for j in range(i+1):
#         print(word[j],end = "")
#     print()

# ---------------------------------------------------------------------
#  Program 71

#      P
#     Py
#    Pyt
#   Pyth
#  Pytho
# Python

# word= input("Enter the word: ")
# for i in range(len(word)):
#     for j in range(len(word)-i-1):
#         print(" ",end ="")
#     for j in range(i+1):
#         print(word[j],end ="")
#     print()

# --------------------------------------------------------------
# Program 72

#      P
#     yy
#    ttt
#   hhhh
#  ooooo
# nnnnnn

# word= input("Enter the word: ")
# for i in range(len(word)):
#     for j in range(len(word)-i-1):
#         print(" ",end ="")
#     for j in range(i+1):
#         print(word[i],end ="")
#     print()

# -----------------------------------------------------
#  Program 73

# Python
# Pytho
# Pyth
# Pyt
# Py
# P

# word= input("Enter the word: ")
# for i in range(len(word),0,-1):
#     for j in range(i):
#         print(word[j],end ="")
#     for j in range(len(word)-i):
#         print(" ",end ="")
#     print()

# ----------------------------------------------------------

# Program 74

# PPPPPP
# yyyyy
# tttt
# hhh
# oo
# n

# word= input("Enter the word: ")
# for i in range(len(word)):
#     for j in range(len(word)-i):
#         print(word[i],end = "")
#     for j in range(i):
#         print(" ",end = "")
#     print()

# --------------------------------------------------------
#  Program 75

# nnnnnn
#  ooooo
#   hhhh
#    ttt
#     yy
#      P
#
#
# word= input("Enter the word: ")
# for i in range(len(word)):
#     for j in range(i):
#         print(" ", end = "")
#     for j in range(len(word)-i,0,-1):
#         print(word[len(word)-(i+1)],end = "")
#     print()

# ---------------------------------------------------------
# Program 76

# nohtyP
#  nohty
#   noht
#    noh
#     no
#      n

# word = input("Enter the word: ")
#
# for i in range(len(word)):
#     for j in range(i):
#         print(" ",end ="")
#     for j in range(len(word)-i):
#         print(word[len(word)-j-1],end ="")
#     print()

# --------------------------------------------------------------
#  Program 77

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# num =int(input("Enter the number of rows: "))
#
# for i in range(num):
#     for j in range(i+1):
#         print(j+1,end = " ")
#     print()

# -----------------------------------------------------------------------
# Program 78
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# num =int(input("Enter the number of rows: "))
#
#
# for i in range(num):
#     k= i+1
#     for j in range(i+1):
#         print(k,end = " ")
#         k=k-1
#     print()

# -------------------------------------------------------------
#  Program 79

# 1
# 2 2
# 3 3 3
# 4 4 4 4

# num= int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(i+1):
#         print(i+1,end = " ")
#     print()

# ----------------------------------------------------------------

# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

# num= int(input("Enter the number of rows: "))
#
# for i in range(num):
#     k=num-i
#     for j in range(i+1):
#         print(k,end = " ")
#     print()

# -------------------------------------------------------------

# Program 79
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

# num= int(input("Enter the number of rows: "))
#
#
# for i in range(num):
#     k=num
#     for j in range(i+1):
#         print(k,end = " ")
#         k =k-1
#     print()

# ------------------------------------------------------------------
#  Program 80

# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

# num= int(input("Enter the number of rows: "))
#
#
# for i in range(num):
#     k=num-i
#     for j in range(i+1):
#         print(k,end = " ")
#         k =k+1
#     print()

# ------------------------------------------------------------------
#  Program 81
#     1
#    12
#   123
#  1234
# 12345


# num= int(input("Enter the number of rows: "))
#
#
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         print(j+1,end ="")
#     print()

# --------------------------------------------------------------
# Program 81

#     1
#    21
#   321
#  4321
# 54321

# num= int(input("Enter the number of rows: "))
#
#
# for i in range(num):
#     k = i+1
#     for j in range(num-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         print(k,end ="")
#         k =k-1
#     print()

# --------------------------------------------------------------------

#  Program 82
#     1
#    22
#   333
#  4444
# 55555

# num= int(input("Enter the number of rows: "))
#
# for i in range(num):
#     k = i+1
#     for j in range(num-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         print(k,end ="")
#     print()

# ----------------------------------------------------------
#  Program 81

#     5
#    44
#   333
#  2222
# 11111
#
# num= int(input("Enter the number of rows: "))
#
# for i in range(num):
#     k = num-i
#     for j in range(num-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         print(k,end ="")
#     print()

# ----------------------------------------------------------
#  Program 82

#     5
#    54
#   543
#  5432
# 54321
#
# num= int(input("Enter the number of rows: "))
#
# for i in range(num):
#     k = num
#     for j in range(num-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         print(k,end ="")
#         k= k-1
#     print()


# ----------------------------------------------------------
#  Program 83

#     5
#    45
#   345
#  2345
# 12345
#
# num= int(input("Enter the number of rows: "))
#
# for i in range(num):
#     k = num-i
#     for j in range(num-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         print(k,end ="")
#         k= k+1
#     print()

# -------------------------------------------------------------------------
# Program 84

#    1
#   1 2
#  1 2 3
# 1 2 3 4

# num = int(input("Enter the number of rows:"))
#
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ", end="")
#     for j in range(i+1):
#         print(j+1,end = " ")
#     print()


# --------------------------------------------------------------
# Program 85

#     1
#    2 1
#   3 2 1
#  4 3 2 1
# 5 4 3 2 1

# num= int(input("Enter the number of rows: "))
#
#
# for i in range(num):
#     k = i+1
#     for j in range(num-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         print(k,end =" ")
#         k =k-1
#     print()

# ------------------------------------------------------------
# Program 86

# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1
#
#
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(i):
#         print(" ",end = "")
#     for j in range(num-i):
#         print(j+1,end = " ")
#     print()

# ----------------------------------------------------------------
# Program 87

# 6 6 6 6 6 6
#  5 5 5 5 5
#   4 4 4 4
#    3 3 3
#     2 2
#      1


# num = int(input("Enter the number: "))
#
# for i in range(num,0,-1):
#     for j in range(num-i):
#         print(" ",end = "")
#     for j in range(i):
#         print(i, end = " ")
#     print()

# -----------------------------------------------------------------------
# Program 88

# 6 5 4 3 2 1
#  6 5 4 3 2
#   6 5 4 3
#    6 5 4
#     6 5
#      6
#
# num = int(input("Enter the number: "))
# for i in range(num,0,-1):
#     k= num
#     for j in range(num-i):
#         print(" ",end = "")
#     for j in range(i):
#         print(k,end =" ")
#         k=k-1
#     print()

# ------------------------------------------------------------------
# Program 89
