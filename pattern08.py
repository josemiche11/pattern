'''

5              
9 4            4
12 8 3         7 3
14 11 7 2      9 6 2
15 13 10 6 1   10 8 5 1

'''
num= int(input("Enter Amp: "))
jo= num
for i in range(num, 0, -1):
    mic= i+1
    f=jo
    for j in range(num-i+1):
        print(f, " ", end="")
        f= f-mic
        mic=mic+1
    print("\r")
    jo= jo+i-1
