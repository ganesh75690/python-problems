# Program to calculate the sum of array elements using loop

def sum_of_array(arr):
    
    total =0 
    for i in arr:
        
        total += i
        
        return total
arr = [1,2,3,4,5,6,7,8,9,10]

print("Sum of array elements is:", sum_of_array(arr))

