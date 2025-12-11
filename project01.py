# Basic claculator
print("Welcome to the basic Calculator.")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

# Get the user choice
choice = input("choose an operation(1/2/3/4): ")

# Get two numbers from the user
num1=float(input("enter the first number: "))
num2 =float(input("enter the second number: "))

# perform the chosen operation
if choice == "1":
    print(f"the result of addition is: {num1+num2}")
elif choice == "2":
    print(f"the result of Substraction is: {num1-num2}")
elif choice == "3":
    print(f"the result of Multiplication is:{num1*num2}")
elif choice == "4":
    if num2 !=0:
        print(f"the result of Division is:{num1/num2}")
    else:
        print("Error:Division by zero is not allowed.")
else:
    print("Invalid choice")                    