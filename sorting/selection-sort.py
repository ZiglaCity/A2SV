# This module implements the selection sort algorithm and a function to sort people by their heights.
# Selection Sort:
# Selection sort is a simple comparison-based sorting algorithm. It works by dividing the input list into two parts: 
# the sorted part and the unsorted part. The algorithm repeatedly selects the smallest (or largest, depending on the 
# order) element from the unsorted part and moves it to the end of the sorted part. It has a time complexity of O(n^2) 
# for both the best and worst cases, making it inefficient for large datasets.
# Functions:
# - selection_sort(nums): Sorts a list of numbers in ascending order using the selection sort algorithm.
# - sortPeople(names, heights): Sorts a list of people's names based on their heights in descending order.
# Example Usage:
# - selection_sort([3, 1, 4, 1, 5, 9]) -> [1, 1, 3, 4, 5, 9]
# - sortPeople(["Mary", "John", "Emma"], [180, 165, 170]) -> ["Mary", "Emma", "John"]

def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        index = i
        for j in range(i + 1, n):
            if nums[j] < nums[index]:
                index = j
        if index != i:  # Only swap if a smaller element is found
            nums[i], nums[index] = nums[index], nums[i]
    return nums


# using selection sort
def sortPeople(names, heights):
    """
    :type names: List[str]
    :type heights: List[int]
    :rtype: List[str]
    """
    for i in range(len(names)):
        max_index = i
        for j in range(i, len(names)):
            if heights[j] > heights[max_index]:
                max_index = j
                
        heights[i], heights[max_index] = heights[max_index], heights[i]
        names[i], names[max_index] = names[max_index], names[i]
    return names


if __name__ == '__main__':
    print(sortPeople(["Mary","John","Emma"], [180,165,170]))
    # Output: ["Mary","Emma","John"]