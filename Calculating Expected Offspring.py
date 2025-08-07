
def expected_offspring(a, b, c, d, e, f):

    AA_AA_off = a * 2
    AA_Aa_off = b * 2
    AA_aa_off = c * 2
    Aa_Aa_off = d * ((1+2)/2)
    Aa_aa_off = e * ((0+2)/2)
    aa_aa_off = f * 0

    sum = AA_AA_off + AA_Aa_off + AA_aa_off + Aa_Aa_off + Aa_aa_off + aa_aa_off

    return sum

print(expected_offspring(17751, 17146, 19950, 18895, 16563, 17402))