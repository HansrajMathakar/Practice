import sys

def isUnique(s):
    c = {}
    if len(s) > 128:
        return False
    
    for i in c:
        if i in c:
            return False
        c[i] = True
    return True

if __name__ == "__main__":
    print(isUnique(sys.argv[0]))



