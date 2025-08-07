
def complement(DNA):
    comp = ""
    for i in DNA:
        if i == "T":
            comp += "A"
        elif i == "C":
            comp += "G"
        elif i == "G":
            comp += "C"
        else:
            comp += "T"
    return comp

def revpalin (DNA):
    pos = []
    for i in range(len(DNA)- 4):
        temp = DNA[i: i + 4]
        com = complement(temp)
        flip = com[::-1]

        if temp == flip:
            
            pos.append(i+1)
    return pos


        

    
print(revpalin("TCAATGCATGCGGGTCTATATGCAT"))