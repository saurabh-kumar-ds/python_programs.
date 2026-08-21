## enter two number to find maximum number.abs

print("Enter two numbers to find maximum number.")
a=eval(input("Enter 1st number : "))
b=eval(input("Enter 2nd number : "))

if b>a:
    a=a+b
    b=a-b
    a=a-b

print(f"Maximum number is {a}")

## add sub mul mod