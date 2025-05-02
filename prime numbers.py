# Program to print prime numbers up to 100

def is_prime(n):
    
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: 
            
            return False
        
    return True

# Print all prime numbers from 2 to 100
for num in range(5, 50):
    
    if is_prime(num):
        
        print(num, end=" ")      