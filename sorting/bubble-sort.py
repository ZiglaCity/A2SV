
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums


# using bubble sort
def sortPeople( names, heights):
    """
    :type names: List[str]
    :type heights: List[int]
    :rtype: List[str]
    """
    for i in range(len(names) - 1):
        for j in range(len(names) - i - 1):
            if heights[j] < heights[j + 1]:
                heights[j], heights[j + 1] = heights[j + 1], heights[j]
                names[j], names[j + 1] = names[j + 1], names[j]
    return names