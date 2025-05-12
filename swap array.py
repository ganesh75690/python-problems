# Program to swap the values in the array using a function

def swap_array(arr, i, j):
    
    arr[i], arr[j] = arr[j], arr[i] 
    
    # Corrected the syntax for swapping
    
    return arr

arr = [2, 3, 1, 4, 6, 9]

i = 0
j = 2

print("Before swapping:", arr)

print("After swapping:", swap_array(arr, i, j)) 
# Time complexity is O(1)
# Space complexity is O(1)