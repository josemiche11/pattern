'''
 43211234
4*      *
3**    **
2***  ***
1********
2***  ***
3**    **
4*      *

'''
num= int(input("Enter the number: "))
for i in range(-num, num+1, +1):
    if i!=0 and i!=1:
        print("*"*(num-abs(i)+1), end="")
        print("  "*(abs(i)-1), end="")
        print("*"*(num-abs(i)+1), end="")
        print("\r")
