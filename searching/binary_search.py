def binary_search(arr, val):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (right + left) // 2
        print(left, right, mid)
        if val < arr[mid]:
            right = mid - 1
        elif val > arr[mid]:
            left = mid + 1
        else:
            return True
    return False


def bisect_right(arr, val):
    left = 0
    right = len(arr) -1
    while left < right:
        mid = (right + left) // 2

        if val < arr[mid]:
            right = mid

        elif val >= arr[mid]:
            left = mid + 1
    return mid


def bisect_left(arr, val):
    left = 0
    right = len(arr) -1
    while left < right:
        mid = (right + left) // 2

        if val <= arr[mid]:
            right = mid

        elif val > arr[mid]:
            left = mid + 1
    return mid

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7, 7, 7,8,9]
    # print(binary_search(arr, val = 9))
    print(bisect_left(arr, val = 7))
    print(bisect_right(arr, val = 7))


