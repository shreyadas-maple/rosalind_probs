
def parseFASTA(fastaFile):
    id_list = []
    seq_list = []
    data = open(fastaFile).read().replace('\n', '').split(">")
    newdata = data[1:]

    for i in range(0, len(newdata)):
        if newdata[i].startswith("Rosalind"):
            id_list.append(newdata[i][0:13])
            seq_list.append(newdata[i][13:])

    return id_list, seq_list

def gcContent(seq):
    new_seq = seq.replace("\\", "").replace("}", "")
    num_GC = 0
    seq_len = len(seq)
    seq_len2 = len(new_seq)

    for i in range(len(new_seq)):
        if new_seq[i] == 'G' or new_seq[i] == 'C':
            num_GC += 1

    print(new_seq + "\n" + str(num_GC/len(new_seq)))
    return (num_GC/len(new_seq))*100


def maxGCContent(file) :
    id_list, seq_list = parseFASTA(file)
    max_id = ''
    max_GC = 0
    gcpercent = 0

    for index, item in enumerate(seq_list):
        gcpercent = gcContent(item)
        if gcpercent > max_GC:
            max_id = id_list[index]
            max_GC = gcpercent
    return max_id + "\n" + str(max_GC)

print(maxGCContent("rosalind_gc.txt"))


