'''
*****
  ***
    *
  ***
*****

'''

num= int(input("Enter Amp: "))
for jos in range(-num, num+1, +1):
    if jos!=0 and jos!=1:
        print("  "*(num-abs(jos)), end="")
        print("*"*((2*abs(jos))-1))
