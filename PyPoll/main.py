#Python Challenge PyPoll

# Dependencies
import os
import csv

# Variables initially defined
TotVotes = 0
Votes = {}
VotePer = {}

# Path to and open resource csv
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    # Store and skip header row
    csvheader = next(csvreader)

    # Iterate through each row of csv file
    for row in csvreader:

        # Increase Total Votes count
        TotVotes += 1

        # Check if candidate is in Votes dictionary and add additional vote, otherwise create new key with 1 vote
        if str(row[2]) in Votes:
            Votes[str(row[2])] += 1
        else:
            Votes[str(row[2])] = 1

MostVotes = 0

print(TotVotes)

for Candidate in Votes:
    VotePer[Candidate] = round((Votes[Candidate] / TotVotes)*100,2)

    if Votes[Candidate] > MostVotes:
        MostVotes = Votes[Candidate]
        Winner = Candidate

    print(f'{Candidate}: {VotePer[Candidate]}% {Votes[Candidate]}')

print(Winner)