def valid_mountain_array(arr):
    n = len(arr)

    if n < 3:
        return False

    i = 1
    while i < n and arr[i - 1] < arr[i]:
        i += 1

    if i == 1 or i == n:
        return False

    while i < n and arr[i - 1] > arr[i]:
        i += 1

    return i == n
arr = [2, 1]

print(valid_mountain_array(arr))
