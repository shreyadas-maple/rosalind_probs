import math

# Create a function to count the As, Cs, Gs, Us in a sequence
def countNucleotides (sequence):
    A_counts = 0
    C_counts = 0
    U_counts = 0
    G_counts = 0

    for i in sequence:
        if i == "A":
            A_counts += 1
        elif i == "C":
            C_counts += 1
        elif i == "U":
            U_counts += 1
        elif i == "G":
            G_counts += 1
        else:
            return "Invalid character"
        
    return [A_counts, U_counts, C_counts, G_counts]

# Define a function to find the number of perfect matchings in a graph created by a sequence 
def perfectMatch (file):
    # Open a read the file in to get the sequence
    data = open(file).read().replace("\n", "")

    # Grab only the sequence, not the id
    sequence = data[14:]

    # Get the number of each nucleotide
    A_counts, U_counts, C_counts, G_counts = countNucleotides(sequence)

    # Check that #A = #U and #C = #G
    if A_counts != U_counts:
        return "Error: no perfect matchings because # of A and U are not equal"
    if C_counts != G_counts:
        return "Error: no perfect matchings because # of C and G are not equal"
    
    # Create an output file with the pairs
    with open("pmch_answer.txt", 'w') as file:
        # Format the print of the pairs according to instructions
        # The number of perfect macthings is #A! * #C!
        file.write(str(math.factorial(A_counts) * math.factorial(C_counts)))

perfectMatch("rosalind_pmch.txt")
