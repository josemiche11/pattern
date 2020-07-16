'''
********
***  ***
**    **
*      *

'''
num= int(input("Enter amplitude: "))
for josemiche in range(num, 0, -1):
    print("*"*josemiche, end="")
    print("  "*(num-josemiche), end="")
    print("*"*josemiche, end="")
    print("\r")
