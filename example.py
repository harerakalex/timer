from time_profiler import timer


@timer(file_log=True)
def add(a, b) -> int:
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


@timer(exp_time=0.01, file_log=True)
def sample_func() -> list:
    """This function allocates lists a, b and then deletes b."""

    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b

    return a


arr = range(1000000000000)

if __name__ == "__main__":
    add(12, 3)
    binary_search(arr, 100000000)
    search(arr, 100000000)
    sample_func()
