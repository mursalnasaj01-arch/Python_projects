#palindrome(121)

# requesting the user for a number
number=input("enter the number: ")

# check if the first and last digits are the same.
if number==number[::-1]:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome.")    