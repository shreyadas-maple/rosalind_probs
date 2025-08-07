# We are going to solve this problem using dynamic programming

def numberRabbits (n, m):
    # We create a list to store the number of rabbits in each stage of life
    # [0] -> newborns; [1] -> rabbits that are 1-month old; [m-1] -> rabbits that are m-1 months old
    rabbits = [0] * m

    # In the first month, there is 1 rabbit
    rabbits[0] = 1

    # Print the rabbits in the first month
    print(rabbits)

    # We are going to iterate through the months 
    for i in range(1, n):
        # Save the number of new_borns each month
        new_borns = 0
        # Iterate through each life stage, to calculate the number of new_borns
        for j in range (1, m):
            # If there are rabbits that are able to reproduce, then add the new borns
            if rabbits[j] > 0:

                new_borns += rabbits[j]
        
        # We insert new_borns as the first index of the list
        rabbits.insert(0, new_borns)
        # We remove the last index of the last, because in the previous month
        # these are the rabbits that have reached the last month of their life
        rabbits.pop()

        # Print the rabbits in the current month
        print(rabbits)

    # Return the sum of the rabbits for the specific month
    return sum(rabbits)

print(numberRabbits(100, 18))