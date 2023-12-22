def binary_search(arr, value):
    low = 0
    high = len(arr) - 1

    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        iterations += 1

        if mid_value < value:
            low = mid + 1
        elif mid_value > value:
            high = mid - 1
        else:
            return iterations, mid_value

    upper = arr[low] if low < len(arr) else None
    return iterations, upper
