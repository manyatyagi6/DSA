arr = [5, 2, 9, 1, 7]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest element:", largest)