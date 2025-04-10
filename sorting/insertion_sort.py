# Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.
# It works by taking elements from the unsorted part of the array and inserting them into their correct position
# in the sorted part of the array. It is efficient for small datasets or nearly sorted data.

def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


def sortPeople( names, heights):
    """
    :type names: List[str]
    :type heights: List[int]
    :rtype: List[str]
    """
    for i in range(1, len(names)):
        for j in range(i, 0, -1):
            if heights[j] < heights[j - 1]:
                break
            
            heights[j], heights[j - 1] = heights[j - 1], heights[j]
            names[j], names[j - 1] = names[j - 1], names[j]
        
    return names


if __name__ == '__main__':
    print(sortPeople(["Mary","John","Emma"], [180,165,170]))
    # Output: ["Mary","Emma","John"]
    print(sortPeople(["Alice","Bob","Bob"], [155,185,150]))
    print(insertion_sort([180,165,170]))