#sorting three numbers

# requesting the user three numbers
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))

#Sorting numbers
if  a > b:
    a,b=b,a
if a > c: 
    a,c=c,a
if b>c:
    b,c=c,b

#result
print("Sorted Numbers: ",a,b,c)

