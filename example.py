from timer import timer


@timer(file_log=True)
def add(a, b):
    return a + b


@timer()
def binary_search(arr, x) -> str:
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return "Found"

    return "Not found"


@timer(file_log=True, exp_time=2)
def search(arr, x) -> str:
    for i in arr:
        if i == x:
            return "Found"
    return "Not found"


arr = range(1000000000000)

add(12, 3)
binary_search(arr, 100000000)
search(arr, 100000000)
