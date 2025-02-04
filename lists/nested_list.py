if __name__ == '__main__':
    res = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        res.append([name, score])
        
    res = sorted(res, key=lambda x: (x[1],x))
    for i in range(1, len(res)):
        if res[0][1] != res[i][1]:
            j = i
            while j < len(res) and res[i][1] == res[j][1]:
                print(res[j][0])
                j += 1
            break
