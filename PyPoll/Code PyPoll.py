import csv
import os

file_path = os.path.join("PyPoll", "Resources", "election_data.csv")

total_votes = 0
candidate_votes = {}
candidate_percentages = {}
winner = ""

with open(file_path) as election_data:
    csvreader = csv.reader(election_data)

    header = next(csvreader)

    for row in csvreader:

        total_votes += 1

        if row[2] not in candidate_votes:
            candidate_votes[row[2]] = 0

        candidate_votes[row[2]] += 1

    for candidate in candidate_votes:
        candidate_percentages[candidate] = round((candidate_votes[candidate] / total_votes) * 100, 2)

    winner = max(candidate_votes, key=candidate_votes.get)

print("Election Results")
print("---------------------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------------------")
for candidate in candidate_votes:
    print(f"{candidate}: {candidate_percentages[candidate]}% ({candidate_votes[candidate]})")
print("---------------------------------------------")
print(f"Winner: {winner}")
print("---------------------------------------------")

with open("PyPoll/Analysis/Election_Results.txt", "w") as analysis_file:
    analysis_file.write("Election Results\n")
    analysis_file.write("---------------------------------------------\n")
    analysis_file.write(f"Total Votes: {total_votes}\n")
    analysis_file.write("---------------------------------------------\n")
    for candidate in candidate_votes:
        analysis_file.write(f"{candidate}: {candidate_percentages[candidate]}% ({candidate_votes[candidate]})\n")
    analysis_file.write("---------------------------------------------\n")
    analysis_file.write(f"Winner: {winner}\n")
    analysis_file.write("---------------------------------------------\n")
