#Load dependencies
import os
import csv

#Create variables or lists to store data
Candidate = []
Candidate_Votes = []
Total_Votes = 0
Winner_Votes = 0

#Use encoding='utf-8 for Windows
csvpath = os.path.join("..","Resources","PyPoll_Resources_election_data.csv")
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    #FUTURE CODING REFERENCE: Below line adds candidates to list and assigns them a vote
    for row in csvreader:
        Total_Votes += 1
        if  Candidate.count(row[2]) == 0:
            Candidate.append(row[2])
            Candidate_Votes.append(1)
        #FUTURE CODING REFERENCE: Below line adds +1 for every time candidate name appears  
        else:
            Candidate_Votes[Candidate.index(row[2])] += 1

print(f"Election Results \n------------------------- \nTotal Votes: {Total_Votes} \n-------------------------")

#Loop through 4 candidates to declare Winner and respective votes
for n in range(len(Candidate)):
    print(f"{Candidate[n]}: {(100*Candidate_Votes[n]/Total_Votes):.3f}% ({Candidate_Votes[n]})")
    if Candidate_Votes[n] > Winner_Votes:
        Winner = Candidate[n]
        Winner_Votes = Candidate_Votes[n]

#Write Results to .txt file
output_file = os.path.join("..","Analysis","PyPoll.txt")
with open(output_file, "w", encoding='utf-8') as datafile:
    datafile.write(f"Election Results\n-------------------------\nTotal Votes: {Total_Votes}\n-------------------------\n")
    for n in range(len(Candidate)):
        datafile.write(f"{Candidate[n]}: {(100*Candidate_Votes[n]/Total_Votes):.3f}% ({Candidate_Votes[n]})\n")
    datafile.write(f"-------------------------\nWinner: {Winner}\n-------------------------\n")