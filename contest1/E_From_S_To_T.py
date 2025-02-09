from collections import Counter
    
n = int(input())
for i in range(n):
    printed = False
    s = input()
    t = input()
    p = input()

    dic_s = Counter(s)
    dic_t = Counter(t)
    dic_p = Counter(p)

    if any(dic_t[char] > dic_s[char] + dic_p[char] for char in dic_t):
        print("NO")
        
    else:
        it = iter(t)
        if any(c not in it for c in s):
            print("NO")
        else:
            print("YES")
    