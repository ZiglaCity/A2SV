t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    nums = [int(char) for char in s]

    dic = {0: 1}
    total = res = 0
    for i in range(len(nums)):
        total += nums[i]
        key = total - (i + 1)
        if key in dic:
            res += dic[key] 
        
        dic[key] = dic.get(key, 0) + 1
    print(res)

    