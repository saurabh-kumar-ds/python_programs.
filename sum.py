## take two numbers input from user and calculate sum of those numbert to use of function.

def add():
    print("Enter two numbers for addition.")
    a=eval(input("Enter 1st number : "))
    b=eval(input("Enter 2nd number : "))
    return a+b

sum = add()
print(f"Sum of both numbeers is : {sum}")

