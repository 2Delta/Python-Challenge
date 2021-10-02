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

        # Check if candidate is in Votes dictionary and add additional vote, otherwise create new candidate key with 1 vote
        if str(row[2]) in Votes:
            Votes[str(row[2])] += 1
        else:
            Votes[str(row[2])] = 1

MostVotes = 0

# Create Results list for text output
sDivider = '--------------------'
Results= [
    'Election Results',
    sDivider,
    f'Total Votes: {TotVotes}',
    sDivider
]

# Calculate vote percentage of each candidate and determine candidate with most votes as winner
for Candidate in Votes:
    VotePer[Candidate] = round((Votes[Candidate] / TotVotes)*100,2)

    if Votes[Candidate] > MostVotes:
        MostVotes = Votes[Candidate]
        Winner = Candidate

    # Add each candidates percentage and votes to the Results list
    Results.append(f'{Candidate}: {VotePer[Candidate]}% {Votes[Candidate]}')

# Add Winner line to Results list
Results.extend([
    sDivider,
    f'Winner: {Winner}',
    sDivider
])

# Convert each item in Results list into string on new lines
Results = '\n'.join([str(item) for item in Results])

# Print Results
print(Results)

# Write results to text file
txtpath = os.path.join('Analysis','Election_Analysis.txt')
with open(txtpath,'w') as writetxt:
    writetxt.write(Results)