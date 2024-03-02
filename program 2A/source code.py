# Function for nth Fibonacci number
def Fibonacci(n):
 if n == 1:
 return 0
 elif n == 2:
 return 1
 else:
 return Fibonacci(n-1) + Fibonacci(n-2)
count = 1
N = int(input("Enter a value of N : "))
if N<=0:
 print("Invalid Input: Enter a value of N (>0)")
else:
 print("Fibonacci sequence : ")
 while count <= N:
 print(Fibonacci(count),end=' ')
 count = count + 1