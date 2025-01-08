#Finding the given num is even odd.
n=float(input("Enter the number:"))
if n>0:
    print("The number is positive")

    if n%2==0:
        print("The number is even.")

    else:
        print("The number is odd.") 

elif n==0:
    print("The number is zero.")

else:
    print("The number is Negative.")