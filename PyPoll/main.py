import os
import csv

# File path
input_file = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidate_votes = {}


# Read data from the input CSV file
with open(input_file) as in_file:
    reader = csv.reader(in_file)
    header = next(reader)

    # Iterate through each row in the CSV file
    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        # Check if the candidate is already in the dictionary
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            # If not, add the candidate to the dictionary
            candidate_votes[candidate_name] = 1

# Write election results to the output text file
with open (output_file, "w") as out_file: 
    out_file.write(
    f"Election Results\n"
    f"--------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"--------------------------------\n" )

    # Iterate through each candidate and write their results to the file
    for candidate_name, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        out_file.write(f"{candidate_name}: {percentage: .3f}% ({votes})\n")

# Determine the winner and write the result to the file
    winner = max(candidate_votes, key=candidate_votes.get)
    out_file.write(
        f"--------------------------------\n"
        f"Winner: {winner}\n"
        f"--------------------------------\n"
    )

# Read and print the content of the output text file
with open(output_file, "r") as out_file:
    print(out_file.read())

