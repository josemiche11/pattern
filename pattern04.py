'''
*      *
**    **
***  ***
********

'''
num= int(input("Enter the number: "))
for miche in range(1, num+1, +1):
    print("*"*miche, end="")
    print("  "*(num-miche), end="")
    print("*"*miche, end="")
    print("\r")
