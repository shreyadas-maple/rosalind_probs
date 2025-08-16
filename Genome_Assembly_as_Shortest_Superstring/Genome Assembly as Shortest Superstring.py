
def parseFASTA(fastaFile):
    # Save all the sequences in a separate list
    seq_list = []

    # Open the file and replacing all the newlines and split the data where a new sequence starts
    data = open(fastaFile).read().replace('\n', '').split(">")
    newdata = data[1:]

    # Based on when Rosalind appears in the array of data, we append the sequences and IDs to the
    # respective lists
    for i in range(0, len(newdata)):
        seq_list.append(newdata[i][13:])

    # Return the sequence and IDs list
    return seq_list

def overlapSeq (s1, s2, min_overlap):
    # We are checking if the suffix of s1 is the prefix of s2
    max_overlap = min(len(s1), len(s2))

    for i in range(max_overlap, min_overlap - 1, -1):
        #print(s1[-i:])
        #print(s2[:i])
        if s1[-i:] == s2[:i]:
            return i
    return 0
    

def assemblySuperstring (file):
    data = parseFASTA(file)

    nodes_index = list(range(0, len(data)))

    edge_weights = {}

    for i in nodes_index:
        weights = []
        connections = []
        for j in nodes_index:
            if data[i] == data[j]:
                pass
            else:
                m = int(min(len(data[i]), len(data[j])) / 2)
                w = (overlapSeq(data[i], data[j], m))

                if w != 0:
                    weights.append(w)
                    connections.append([i, j])

        edge_weights[i] = weights

    for i in edge_weights.keys():
        print(i, ":", edge_weights[i])

    


assemblySuperstring("rosalind_long.txt")




