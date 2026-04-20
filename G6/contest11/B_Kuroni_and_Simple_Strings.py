s = input()
stack = []
res = []
for i in range(len(s)):
    if stack and s[i] == ')':
            if res and stack[-1] < res[-1]: 
                pass
            else:
                res.append(stack.pop())
                res.append(i + 1)
    if s[i] == '(':
        stack.append(i + 1)

print(len(res))
print(*res)

