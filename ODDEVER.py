def check(n):
    if(n<2):
        return(n%2 == 0)
    return(check(n-2))

n = int(input("Enter a number: "))

if(check(n) == True):
    print("the number is even")
else:
    print("the number is odd")
