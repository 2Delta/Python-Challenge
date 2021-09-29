# Python-Challenge PyBank

# Dependencies
import os
import csv

# Variables initially defined
TotMonths = 0
NetTotal = 0
PrevValue = 0
IncDiff = 0
DecDiff = 0
Change = []

# Path to and open resource csv
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    # Store and skip header row
    csvheader = next(csvreader)

    # Iterate through each row of csv file
    for row in csvreader:
        
        # Increase month count
        TotMonths += 1

        # Add to net total
        NetTotal += int(row[1])
        
        # Calculate change in profit/loss from previous month and append to list Change
        Diff = int(row[1]) - PrevValue
        Change.append(Diff)

        # Check if greatest increase and store values
        if Diff > IncDiff:
            IncMonth = str(row[0])
            IncDiff = Diff

        # Check if greatest decrease and store values
        if Diff < DecDiff:
            DecMonth = str(row[0])
            DecDiff = Diff
        
        # Store current row profit/loss for use in next row change in calculation
        PrevValue = int(row[1])

# Function returns arithmatic mean
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

# Calculate average for Changes
AvgChange = round(average(Change),2)

# Store output strings
sTotMonths = str(f'Total Months: {TotMonths}')
sNetTotal = str(f'Total: ${round(NetTotal,2)}')
sAvgChange = str(f'Average Change: ${AvgChange}')
sInc = str(f'Greatest Increase in Profits: {IncMonth} ${IncDiff}')
sDec = str(f'Greatest Decrease in Profits: {DecMonth} ${DecDiff}')
lines = ['Financial Analysis', '--------------------',sTotMonths, sNetTotal, sAvgChange, sInc, sDec]

# Print ouput strings
print('\n'.join(lines))

# Write to text file in Analysis folder
txtpath = os.path.join('Analysis','Financial_Analysis.txt')
with open(txtpath,'w') as writetxt:
    writetxt.write('\n'.join(lines))