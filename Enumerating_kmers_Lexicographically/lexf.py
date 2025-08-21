from itertools import product

def kmers_Lexi (file):
    data = open(file).read().replace('\n', ' ').split(" ")

    symbols = data[:-2]
    n_len = int(data[-2])

    partial_perms = product(symbols, repeat=n_len)
    
    # Create an output file with counts
    with open("lexf_ans.txt", 'w') as file:
        # Format the print of the pairs according to instructions
        for perms in partial_perms:
            line = ""
            for set in perms:
                line += set
            line += "\n"
            file.write(line)
    


kmers_Lexi("rosalind_lexf.txt")