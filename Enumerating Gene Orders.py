from itertools import permutations
import numpy as np

def permut(num):

    perm = permutations(range(1, num + 1))
    count = 0

    empty = []

    for i in list(perm):
        count += 1
        empty.append(i)

    print(count)

    for tup in empty:
        line = ""
        for i in list(tup):
            line += str(i) + " "
        print(line)

    ##print("\n" + str(empty))



permut(7)