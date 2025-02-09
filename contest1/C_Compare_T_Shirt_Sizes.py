t = int(input())
less = '<'
greater = '>'
equal = '='

for i in range(t):
    a, b = map(str, input().split())
    dic_a = {'S':-1, 'M': 0 , 'L':1}    
    dic_b = {'S':-1, 'M': 0 , 'L':1}    
    if a[-1] == 'S':
        dic_a[a[-1]] -= (len(a) - 1)
    elif a[-1] == 'L':
        dic_a[a[-1]] += (len(a) - 1)
    if b[-1] == 'S':
        dic_b[b[-1]] -= (len(b) - 1)
    elif b[-1] == 'L':
        dic_b[b[-1]] += (len(b) - 1)
        
    if dic_a[a[-1]] > dic_b[b[-1]]:
        print('>')
    elif dic_a[a[-1]] < dic_b[b[-1]]:
        print('<')
    else:
        print('=')
