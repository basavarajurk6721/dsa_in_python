def k_largest_elements(arr, k):
    count = 0
    for num in arr:
        if num > k:
            count += 1
    return count
arr = [10, 20, 30, 40, 50]
k = 25
result = k_largest_elements(arr, k)
print("The number of elements greater than", k, "is:", result)