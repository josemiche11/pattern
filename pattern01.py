'''
 123456789123456789
1    *        *
2   ***      ***
3  *****    *****
4 *******  *******
5******************

'''
num= int(input("Enter the number : "))
for i in range(1, num+1, +1):
    print(" "*(num-i), end="")
    print("*"*(2*(i-1)+1), end="")
    print(" "*((num-i)*2), end="")
    print("*"*(2*(i-1)+1), end="")
    print("\r")
