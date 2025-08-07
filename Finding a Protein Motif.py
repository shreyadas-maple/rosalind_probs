from urllib.request import urlopen
def getfasta(uniprot_id):
    url = "http://www.uniprot.org/uniprot/" + uniprot_id[:6] +".fasta"
    page = urlopen(url).read().decode('utf-8').split("\n")
    fasta = page[1:]
    fasta_seq = "".join(fasta)
    loc = []
    prot_seq = []
    ##print(fasta_seq)
    ##print(fasta_seq[84:89], fasta_seq[117:122], fasta_seq[141:146], fasta_seq[305:310], fasta_seq[394:399])
    ##print(fasta_seq[46:51], fasta_seq[114:119], fasta_seq[115:120], fasta_seq[381:386], fasta_seq[408:413])

    for i in range(len(fasta_seq)):
        if fasta_seq[i] == "N" and fasta_seq[i+1] != "P" and (fasta_seq[i + 2] == "S" or fasta_seq[i+2] == "T") and fasta_seq[i+3] != "P":
            loc.append(i+1)
            prot_seq.append(fasta_seq[i:i+4])
    return loc
    ##print(prot_seq)

def domain(FASTA_file):
    file = open(FASTA_file, "r").read().split("\n")
    ids = []


    for line in file:
        ids.append(line)

    for id in ids:
        prot_loc = getfasta(id)
        if prot_loc != []:
            print(id)
            for loc in prot_loc:
                print(str(loc) + " ", end="")
            print("")

domain("rosalind_mprt.txt")

