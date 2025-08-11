def findSubPerm (n, pi):

    increase = []
    long_increase = []
    decrease = []

    small_curr = pi[0]

    large_curr = pi[0]

    for i in range(n):
        if small_curr <= pi[i]:
            print(small_curr, " < ", pi[i])
            small_curr = pi[i]
            increase.append(pi[i])
        else:
            print("Change")
            increase = []
            small_curr = pi[i]
            increase.append(pi[i])
    
    print(increase)
    """
    # Find the index of the smallest number in the list
    smallest_index = pi.index(min(pi))

    # Add this number to the increasing list
    increase.append(pi[smallest_index])

    #print(smallest_index)

    curr = pi[smallest_index]

    for i in range(smallest_index, n):
        if curr < pi[i]:
            if i == n - 1:
                increase.append(pi[i])
            else:
                if pi[i] < pi[i + 1]:
                    curr = pi[i]
                    increase.append(pi[i])

    largest_index = pi.index(max(pi))

    decrease.append(pi[largest_index])

    curr = pi[largest_index]

    for i in range(largest_index, n - 1):
        if curr > pi[i]:
            if (i == n - 2) and pi[i] < pi[i + 1]:
                    decrease.append(pi[i])
            else:
                if pi[i] > pi[i + 1]:
                    curr = pi[i]
                    decrease.append(pi[i])

    print (increase, "\n", decrease)
    #return increase

    """



findSubPerm(5, [5, 1, 3, 4, 2])