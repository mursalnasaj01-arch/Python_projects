# Find median of a list

numbers=sorted(map(int,input("enter a list of numbers separated by spaces: ").split()))
n=len(numbers)
if n % 2 ==0:
    median = (numbers[n//2-1] +numbers[n//2]) /2
else:
    median =numbers[n//2] 
print(f"the median is: {median}")       