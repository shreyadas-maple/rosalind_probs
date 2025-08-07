def parseFASTA(fastaFile):
    ## Save all the sequences in a separate array
    seq_list = []

    ## Open the file and replacing all the newlines and split the data where a new sequence starts
    data = open(fastaFile).read().replace('\n', '').split(">Rosalind_")
    newdata = data[1:]

    ## Based on when Rosalind appears in the array of data, we sort into  sequences
    for i in range(0, len(newdata)):
        seq_list.append(newdata[i][4:])

    ## Since we are only going to use the sequence array, return the sequence array only
    return seq_list


def consensus(fastaFile):
    seq_list = parseFASTA(fastaFile)
    n = len(seq_list)
    As = []
    Cs = []
    Gs = []
    Ts = []

    con_seq = ""

    for i in range(len(seq_list[0])):
        A = 0
        C = 0
        G = 0
        T = 0
        for j in range(n):
            if seq_list[j][i] == "A":
                A += 1
            elif seq_list[j][i] == "C":
                C += 1
            elif seq_list[j][i] == "G":
                G += 1
            else:
                T += 1
        As.append(A)
        Cs.append(C)
        Gs.append(G)
        Ts.append(T)

    for y in range(len(seq_list[0])):
        if As[y] > Cs[y] and As[y] > Gs[y] and As[y] > Ts[y]:
            con_seq += "A"
        elif Cs[y] > As[y] and Cs[y] > Gs[y] and Cs[y] > Ts[y]:
            con_seq += "C"
        elif Gs[y] > As[y] and Gs[y] > Cs[y] and Gs[y] > Ts[y]:
            con_seq += "G"
        elif Ts[y] > As[y] and Ts[y] > Cs[y] and Ts[y] > Gs[y]:
            con_seq += "T"
        elif As[y] == Cs[y] or As[y] == Gs[y] or As[y] == Ts[y]:
            con_seq += "A"
        elif Cs[y] == Gs[y] or Cs[y] == Ts[y]:
            con_seq += "C"
        else:
            con_seq += "G"
    print(con_seq, end=' \n')
    print("A: ", end='')
    for a in As:
        print(a, end=' ')
    print()
    print("C: ", end='')
    for c in Cs:
        print(c, end=' ')
    print()
    print("G: ", end='')
    for g in Gs:
        print(g, end=' ')
    print()
    print("T: ", end='')
    for t in Ts:
        print(t, end=' ')




consensus("rosalind_cons.txt")

