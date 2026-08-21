## enter two number to find minimum number.

print("Enter two numbers to find minimum number.")
a=eval(input("Enter 1st number : "))
b=eval(input("Enter 2nd number : "))

if b>a:
    a=a+b
    b=a-b
    a=a-b

print(f"miniimum number is {b}")

## what to think.