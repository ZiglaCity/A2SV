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

    for i in dic_t:
        if dic_t[i] > dic_s[i] + dic_p[i]:
            print("No")
            
        else:
            it = iter(t)
            if any(c not in it for c in s):
                print("No")
            else:
                print("Yes")
    