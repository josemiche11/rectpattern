'''
 43211234
4********
3*** ****
2**   ***
1*     **
1**     *
2***   **
3**** ***
4********

'''
num= int(input("Enter Amplitude : "))
print("*"*(2*num))
for i in range(num-1):
    print("*"*(num-i-1), end="")
    print(" "*((2*i)+1), end="")
    print("*"*(num-i), end="")
    print("\r")
for j in range(num-1, 0, -1):
    print("*"*(num-j+1), end="")
    print(" "*(((j-1)*2)+1), end="")
    print("*"*(num-j), end="")
    print("\r")
print("*"*(2*num))
