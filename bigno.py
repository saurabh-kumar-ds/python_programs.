## take two input from user to find biggest number.

print("Enter two numbers to find biggest number.")
num1 = eval(input("Enter 1st number : "))
num2 = eval(input("Enter 2nd number : "))

if num1 > num2:
    print(f"biggest number is {num1}")
else:
    print(f"biggest number is {num2}")