#This code for linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Element found at index {i}" 
    return "Element not found"  

arr = [10, 20, 30, 40, 50]
target = 40

print(linear_search(arr, target))  
