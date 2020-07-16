'''
1
6 2            4
10 7 3         7 3
13 11 8 4      9 6 2
15 14 12 9 5   10 8 5 1

'''
num= int(input("Enter Amp: "))
jo=1
for i in range(num, 0, -1):
    mic= i
    f= jo
    for j in range(num-i+1):
        print(f, end=" ")
        f= f-mic
        mic= mic+1
    jo= jo+i
    print("\r")
