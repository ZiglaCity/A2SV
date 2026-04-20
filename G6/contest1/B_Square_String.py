t = int(input())
for i in range(t):
    String = input()

    if len(String) % 2 == 1:
        print("NO")
    else:
        x = len(String)
        half = int(x/2)
        if String[:half] == String[half:]:
            print("YES")
        else:
            print("NO")
        

