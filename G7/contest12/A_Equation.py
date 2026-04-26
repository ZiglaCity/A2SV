n = int(input())

def is_comp(num):
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i: 
            return True
    return False

start = 4
while not (is_comp(start) and is_comp(start + n)):
    start += 1

print(start + n, start)
