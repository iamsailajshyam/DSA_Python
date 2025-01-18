import array as arr
a = arr.array('i',[1,2,3])
print(a[])
#########################
arr = [1,2,3,4,5,6]
for i in range (0, len(arr)):
  print (arr[i])

########################
arr = [[1,2,3],[4,5,6]]
for i in range (0, len(arr)):
  print (arr[i]) 
########################
arr = [[1,2,3],['a','b']]
for i in range (0, len(arr)):
  print (arr[i])
########################
arr = [1, 2, 3, 2, 5, 6]
print(arr [1:4])

########################

arr = [1, 2, 3, 2, 3, 6]
print(arr.count(2))  # Counts how many times the number 2 appears in the lis

########################
#Linner Search
arr = [1, 2, 3, 4, 5, 6]
print(arr[6: :-1])
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Element found at index {i}"
    return "Element not found"

arr = [10, 20, 30, 40, 50]
target = 40

print(linear_search(arr, target))
########################
