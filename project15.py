#Find the GCD of two numbers

def gcd(x,y):
    while y !=0:
        x,y=y,x%y
    return x

num1 = int(input("enter the first number: ")) 
num2 = int(input("enter the second number: "))
print(f"the GCD of {num1} and {num2} is {gcd(num1,num2)}") 

 