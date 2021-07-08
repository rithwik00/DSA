def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while high >= low:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            hgih = mid - 1
        else:
            return mid

    return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binarySearch(arr, x)

if result != -1:
    print(result)
else:
    print('Element not present')