def swap_case(s):
    x = ""
    for char in s:
        var = ord(char)
        if var >= ord('A') and var <= ord("Z"):
            x += chr(var + 32)
        elif var >= ord('a') and var <= ord('z'):
            x += chr(var - 32)
        else:
            x += char

    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
