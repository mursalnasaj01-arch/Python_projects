# Find the LCM of two numbers

def lcm(x,y):
    greater=max(x,y)
    while True:
        if greater % x==0 and greater % y ==0:
            return greater
        greater +=1

#requesting two numbers from user
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))

# result
print(f"the LCM of {a} and {b} is {lcm(a,b)}")    


 
