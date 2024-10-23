# Read the number of rounds

N = int(input())



# Initialize cumulative scores and variables to track the maximum lead and winner

sum_1 = 0

sum_2 = 0

max_lead = 0

winner = 0



# Iterate through each round

for _ in range(N):

    # Read the scores for both players in the current round

    S, T = map(int, input().split())

    

    # Update the cumulative scores

    sum_1 += S

    sum_2 += T

    

    

    # Calculate the lead for the current round

    if sum_1 > sum_2:

        lead = sum_1 - sum_2

        if lead > max_lead:

            max_lead = lead

            winner = 1  # Player 1 is the leader

    else:

        lead = sum_2 - sum_1

        if lead > max_lead:

            max_lead = lead

            winner = 2  # Player 2 is the leader



# Print the winner and the maximum lead

print(winner, max_lead)
