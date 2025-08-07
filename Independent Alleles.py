from scipy.stats import binom
# You can use binomial distribution to solve for "at least" probabilities

def indep_alleles_1(k, N):
    # Define parameters
    n = 2 ** k # The number of trials
    p = 0.25 # The probability of success or probability of getting Aa Bb offspring

    # Save the probabilities in a list to use later
    probabilities = []


    for i in range(N):
        # Calculate all P(X < N) using pmf and append to the probabilities list
        probabilities.append(binom.pmf(i, n, p))


    # To calculate the probability of at least N, we sum the probabilities of all in range
    # of N and subtract it from 1. This is known as the complement rule in statistics.
    prob_of_least_N = 1 - (sum(probabilities))

    # Return the calculated probability
    return prob_of_least_N

print(f"{indep_alleles_1(6, 18):.3f}")
