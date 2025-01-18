"""Binnary Search"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if arr[mid] == target:
            return f"Element found at index {mid}"  # Best-case scenario
        elif arr[mid] < target:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half

    return "Element not found"  # If the target is not in the list

# Example usage
arr = [10, 20, 30, 40, 50, 60]
target = 30

print(binary_search(arr, target))  # Best-case: Element found at index 2
