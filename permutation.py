import sys
import operator

def isPermutation(s1, s2):
    input1, input2 = [], []

    for i in s1:
        input1.append(i)

    for j in s2:
        input2.append(j)

    input1.sort()
    input2.sort()

    if operator.eq(input1, input2):
        return True
    return False

if __name__ == "__main__":
    print(isPermutation(sys.argv[-1], sys.argv[-2]))