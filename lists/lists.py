if __name__ == '__main__':
    N = int(input())
    commands = []
    for i in range(N):
        c = input().split()
        commands.append(c)
     
    res = []   
    for command in commands:
        if 'insert' in command:
            res.insert(int(command[1]), int(command[2]))
        elif 'print' in command:
            print(res)
        elif 'remove' in command:
            res.remove(int(command[1]))
        elif 'append' in command:
            res.append(int(command[1]))
        
        elif 'sort' in command:
            res.sort()
        elif 'pop' in command:
            res.pop()
        else:
            res.reverse()