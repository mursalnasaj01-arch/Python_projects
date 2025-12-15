# Sum of Digit

num=int(input("enter a number: "))
total=0

for digit in str(num):
    total +=int(digit)

print(total)    
