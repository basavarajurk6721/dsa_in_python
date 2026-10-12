def even_odd(arr):
    even_numbers = 0
    odd_numbers = 0

    for num in arr:
        if num %2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
    return even_numbers, odd_numbers
arr = [10, 25, 30 ,45 ,50, 65, 70]

even ,odd = even_odd(arr)
print("The even numbers in the array is:", even)
print("The odd numbers in the array is:", odd)