import sys

def urlify(s, l):
    res = list(s)
    length = len(s)
    x = False
    for i in reversed(s):
        if i != " ":
            res[length - 1] = i
            length -= 1
            x = True
        elif x:
            res[length - 1] = "0"
            res[length - 2] = "2"
            res[length - 3] = "%"
            length -= 3

    op = ''.join(res)
    return op

    

if __name__ == "__main__":
    print(urlify(sys.argv[-2], sys.argv[-1]))

