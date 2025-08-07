

def numberRabbits (n, k):

    if n == 1 or n == 2:
        return 1
    else:
        twoGen = numberRabbits(n - 2, k)
        oneGen = numberRabbits(n - 1, k)

        return twoGen * k + oneGen

print(numberRabbits(32, 2))