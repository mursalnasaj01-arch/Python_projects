#Check if string only contain  digits

text=input("enter a string: ")
if text.isdigit():
    print(f"{text} contains only digits.") 
else:
    print(f"{text} does not contain only digits.")     