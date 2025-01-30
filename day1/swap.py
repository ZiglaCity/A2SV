def swap_case(s):
    x = ""
    for char in s:
        var = ord(char)
        if var > 96 and var < 122:
            x += chr(var - 32)
        elif var > 64 and var < 90:
            x += chr(var + 32)
        else:
            x += char

    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
