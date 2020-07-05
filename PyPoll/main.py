import os
import csv

# path to budget_data
electionCsvPath = os.path.join('Resources', 'election_data.csv')

# read data then sorted by Candidate
with open(electionCsvPath, 'r', newline='') as fileInput:

    # read data
    csvreader = csv.reader(fileInput, delimiter = ",")
    
    # read 1st row
    csv_header = next(csvreader)
    candidateList = {}
    totalVotes = 0

    # loop thorugh each row
    for row in csvreader:
        totalVotes +=1
        curCandidate = row[2]

        if curCandidate not in candidateList:
            candidateList[curCandidate] = 1
        else:
            candidateList[curCandidate] = candidateList[curCandidate] +1
        
#    Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

print("ELection Results")
print("------------------------")
print(f"Total Votes: {totalVotes}")
print("------------------------")

for Candidate, vote in candidateList.items():
    print(f"{Candidate}:  {round(vote/totalVotes*100,3)}% ({vote})")

print("------------------------")
print(f"Winner: {max(candidateList, key=candidateList.get)}") 
print("------------------------")
    