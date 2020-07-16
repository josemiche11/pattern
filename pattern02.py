'''
 12345678912345678912345
1     *           *
2    * *         * *
3   * * *       * * *
4  * * * *     * * * *
5 * * * * *   * * * * *
6* * * * * * * * * * * *

'''
num= int(input("Enter the number: "))
for j in range(1, num+1, +1):
    print(" "*(num-j), end="")
    print("* "*j, end="")
    print("  "*(num-j), end="")
    print("* "*j, end="")
    print("\r")
