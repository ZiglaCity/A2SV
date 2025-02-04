t = int(input())
less = '<'
greater = '>'
equal = '='
dic = {'S':-1, 'M': 0 , 'L':1}    
for i in range(t):
    a, b = map(str, input().split())
    if a[-1] == 'S':
        dic[a] -= (len(a) - 1)
    elif a[-1] == 'L':
        dic[a] += (len(a) - 1)
    if b[-1] == 'S':
        dic[b] -= (len(b) - 1)
    elif b[-1] == 'L':
        dic[b] += (len(b) - 1)
        
    if dic[a] > dic[b]:
        print('>')
    elif dic[a] < dic[b]:
        print('<')
    else:
        print('=')