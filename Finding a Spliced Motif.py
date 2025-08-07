
def findstrinDNA(fasta_file):
    data = open(fasta_file, "r").read().replace("\n", "").split(">Rosalind_")

    s = data[1]
    t = data[2]

    s = s[4:]
    t = t[4:]

    nos = 0
    num = ""

    for char in t:
        ##print(char)
        for n in range(len(s)):
            if s[n] == char and n > nos:
                nos = n
                char += char
                ##print("nos:" + str(nos))
                num += str(n+1) + " "
                ##print(n+1)
    return(num)
    

print(findstrinDNA("rosalind_sseq.txt"))

