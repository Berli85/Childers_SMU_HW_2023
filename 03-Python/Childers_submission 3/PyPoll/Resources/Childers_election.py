#Import files
import os
import csv

#Create filepath to csv data
FilePath = "Childers_submission 3/PyPoll/Resources/Childers_election_data.csv"

#Declare variables
total_Votes = 0

#Create dictionary of candidates
candidate_dictionary = {}

#Read the csv file data
with open(FilePath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the top row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read rows after the header
    for row in csvreader:

        #Count votes
        total_Votes = total_Votes + 1

        #Store candidates and add 1 if candidate name is in the dictionary
        candidate_name = row[2]

        if candidate_name in candidate_dictionary.keys():
                candidate_dictionary[candidate_name] = candidate_dictionary[candidate_name] + 1
        else:
                candidate_dictionary[candidate_name] = 1

#Find which candidate won
winner_vote = 0
winner = ""

#Compare votes
for candidate_name in candidate_dictionary.keys():
    votes = candidate_dictionary[candidate_name]
    if   votes > winner_vote:
          winner_vote = votes
          winner = candidate_name  
 
#Show total votes
print(total_Votes)
print(candidate_dictionary)
print(winner, winner_vote)

#Export to text file
with open("Childers_electiondata_output_module3.txt", "w") as txt_file:
    output = f"""
Election Results
------------------------------
Total Votes: {total_Votes}
------------------------------\n"""

    for key in candidate_dictionary.keys():
        percent = round(100*candidate_dictionary[key]/total_Votes, 2)
        newLine = f"{key}: {percent}% ({candidate_dictionary[key]})\n"
        output += newLine

    finalLine = f"""
    ------------------------------
        Winner: {winner}
    ------------------------------
    """
    output += finalLine
    print(output)
    txt_file.write(output)

    