def split_and_join(line):
    # write your code here
    x = ""
    for char in line:
        if char == " ":
            x += "-"
        else:
            x += char
    return x
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)