# Program to print Fibonacci numbers

def fibonacci(n):
    a, b = 0, 1
    
    if n <= 0:
        
        return 0
    
    elif n == 1:
        
        return 1
    
    else:
        
        for _ in range(2, n + 1):
            a, b = b, a + b
            
        return b

# Print Fibonacci numbers up to the 20th term
n = 10

print("Fibonacci numbers are:", end=" ")
for i in range(n):
    print(fibonacci(i), end=" ")