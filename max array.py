
#python program to find maximum element in a array 

def max_array(arr):
    
    #initialize max to first element
    
    max=arr[0]
    
    #traverse the array 
    
    for i in range(1,len(arr)):
        
        #compare each element with max
        
        if arr[i]> max:
            
            max=arr[i]
            return max
        
#test the function
arr=[1,97,31,4,5]                                               

print("maximum is",max_array(arr)) 

#time complexity is O(n)             
#space complexity is O(1)           