
def longSubseq(n, pi):

    min_num = min(pi)
    min_num_id = pi.index(min_num)
    max_num = max(pi)
    max_num_id = pi.index(max_num)

    increase = []
    decrease = []

    increase.append(min_num)
    decrease.append(max_num)

    for i in pi[min_num_id:]:
        if pi[i] > min_num and (i == len(pi)) or (pi[i + 1] > pi[i]):
            increase.append(i)
            min_num = i

    print(increase)

    for j in pi[max_num_id:]:
        print(j)
        if j < max_num and (j + 1 < j):
            decrease.append(j)
            max_num = j

    print(decrease)

longSubseq(5, [5, 1, 4, 2, 3])
