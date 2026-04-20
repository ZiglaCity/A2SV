[]

# megrge sort but with extra space in each recursive stack
def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return arr 
    
    def merge(arr1, arr2):
        i = j = k = 0
        res = [0] * (len(arr1) + len(arr2))
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res[k] = arr1[i]
                i += 1
            else:
                res[k] = arr2[j]
                j += 1
            k += 1
        
        while i < len(arr1): res[k] = arr1[i]; i += 1; k += 1
        while j < len(arr2): res[k] = arr2[j]; j += 1; k +=1
        return res

    def sort(arr):
        if len(arr) <= 1:
            return arr
        
        part1 = sort(arr[: len(arr)//2])[:]
        print("Part1", part1)
        part2 = sort(arr[len(arr)//2:])[:]
        print("Part2", part2)
        return merge(part1, part2)[:]
        
    return sort(arr)


if __name__ == "__main__":
    arr = [4, 6, 3, 2, 7, 4, 2, 8, 4, 7, 9, 6, 3, 0]
    print(mergeSort(arr))