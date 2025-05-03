n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

a.sort(reverse=True)
total_cost = sum(a)
for qi in q:
    discount = a[qi - 1]    
    print(total_cost - discount)
