'''
         *
        * *
       * * *
      * * * *
     * * * * *
    *         *
   * *       * *
  * * *     * * *
 * * * *   * * * *
* * * * * * * * * *

'''
num= int(input("Enter the number: "))
for jo in range(1, num+1, +1):
    print(" "*num, end="")
    print(" "*(num-jo), end="")
    print("J "*jo)
for mi in range(1, num+1, +1):
    print(" "*(num-mi), end="")
    print("J "*mi, end="")
    print("  "*(num-mi), end="")
    print("J "*mi)
