def largest_element(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num
    return largest
arr = [20,10,30,5,40]
result = largest_element(arr)
print("The largest element in the array is:", result)