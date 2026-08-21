## Take two input to calculate difference.abs

a=eval(input("Enter 1st number : "))
b=eval(input("Enter 2nd number : "))

if b>a:
    a=a+b
    b=a-b
    a=a-b

print(f"difference is {a-b}")