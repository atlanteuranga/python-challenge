import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#initialize variables

total_votes = 0
candidate_dict ={"candidates":[], "votes":[], "percentages":[]}
new_candidate = ""
candidate_votes = 0

#open csv file to start reading it
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #store the header
    header = next(csvreader)

    #iterate through the rows
    for row in csvreader:
        #find a new candidate
        if row[2] not in candidate_dict["candidates"]:
            new_candidate = row[2]
            candidate_dict["candidates"].append(row[2])
        total_votes += 1
    


    for candidate in candidate_dict["candidates"]:
        with open(csvpath, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter = ',')

            #store the header
            header = next(csvreader)
            for row in csvreader:
                if row[2] == candidate:
                    candidate_votes = candidate_votes + 1

        candidate_dict["votes"].append(candidate_votes)
        candidate_dict["percentages"].append("{:.3%}".format(candidate_votes/total_votes))
        candidate_votes = 0


    # print(candidate_dict["candidates"])
    # print(candidate_dict["votes"])
    # print(candidate_dict["percentages"])

    winner_index = 0
    for x in range(len(candidate_dict["votes"])):
        if candidate_dict["votes"][x] > candidate_dict["votes"][winner_index]:
            winner_index = x
    
    winner = candidate_dict["candidates"][winner_index]

    print("Election Results:"
    print("---------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------")
    for i in range(len(candidate_dict["candidates"])):
        print(f"{candidate_dict['candidates'][i]}: {candidate_dict['percentages'][i]} ({candidate_dict['votes'][i]})")
    print("---------------------")
    print("Winner: " + winner)
    print("---------------------")

    file = os.path.join('analysis', 'PyPoll.txt')

    with open(file,'w') as text:
        text.write("Election Results: \n---------------------\n")
        text.write(f"Total Votes: {total_votes} \n---------------------\n")
        for i in range(len(candidate_dict["candidates"])):
            text.write(f"{candidate_dict['candidates'][i]}: {candidate_dict['percentages'][i]} ({candidate_dict['votes'][i]})\n")
        text.write("---------------------\nWinner: " + winner+"\n---------------------")

    
    
                
        