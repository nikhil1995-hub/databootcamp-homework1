import os
import csv
import math

#Locate file
electiondata_csv=os.path.join("./Resources/election_data.csv")

#Set Lists and Variables 
total_votes=[]
total_candidates=[]

khan_votes= 0
correy_votes=0
li_votes=0
otooley_votes=0



#Open/read file 
with open(electiondata_csv, newline="",encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    nextreader=next(csvreader)

#Begin iterator for total votes and candidates  
    for row in csvreader:
        #print(row)
        total_votes.append(row[0])
        total_candidates.append(row[2]) 

        if row[2]=="Khan":
            khan_votes+=1
            #print(row[2])
        elif row[2]=="Correy":
            correy_votes+=1
        elif row[2]=="O'Tooley":
            otooley_votes+=1
        elif row[2]=="Li":
            li_votes+=1

#percentage for each candidate
print(khan_votes)
percentage_khan= round((khan_votes/(len(total_votes)))*100,2)
print (int(percentage_khan))

print(correy_votes)
percentage_correy= round((correy_votes/(len(total_votes)))*100, 2)
print (int(percentage_correy))

print(li_votes)
percentage_li= round((li_votes/(len(total_votes)))*100, 2)
print (int(percentage_li))

print(otooley_votes)
percentage_otooley= round((otooley_votes/(len(total_votes)))*100,2)
print (int(percentage_otooley))


#Max number of votes
candidate_list=[percentage_khan,percentage_correy,percentage_li,percentage_otooley]
max_votes=max(candidate_list)
print(max_votes)

#if statement to determine winner

if max_votes==percentage_otooley:
    winner="O'Tooley"
elif max_votes==percentage_li:
    winner="Li"
elif max_votes==percentage_correy:
    winner="Correy"
else:
    winner="Khan"

print(winner)
#Final Table 

print("                             ")
print ("Election Results")
print ("----------------------------")
print (f"Total Votes: {len(total_votes):}")
print ("----------------------------")
print (f"Khan: {percentage_khan:.3f}% ({khan_votes})")
print (f"Correy: {percentage_correy:.3f}% ({correy_votes})")
print (f"Li: {percentage_li:.3f}% ({li_votes})")
print (f"O'Tooley: {percentage_otooley:.3f}% ({otooley_votes})")
print ("----------------------------")
print (f"Winner:{winner}")
print ("----------------------------")

#Text File Output

finaloutput=os.path.join("./Analysis/finaloutput.txt")

with open(finaloutput,"w") as fileoutput:
    fileoutput.write("                                  ")
    fileoutput.write("\n")
    fileoutput.write("Election Results")
    fileoutput.write("\n")
    fileoutput.write("----------------------------")
    fileoutput.write("\n")
    fileoutput.write (f"Total Votes: {len(total_votes):}")
    fileoutput.write("\n")
    fileoutput.write ("----------------------------")
    fileoutput.write("\n")
    fileoutput.write (f"Khan: {percentage_khan:.3f}% ({khan_votes})")
    fileoutput.write("\n")
    fileoutput.write (f"Correy: {percentage_correy:.3f}% ({correy_votes})")
    fileoutput.write("\n")
    fileoutput.write (f"Li: {percentage_li:.3f}% ({li_votes})")
    fileoutput.write("\n")
    fileoutput.write (f"O'Tooley: {percentage_otooley:.3f}% ({otooley_votes})")
    fileoutput.write("\n")
    fileoutput.write ("----------------------------")
    fileoutput.write("\n")
    fileoutput.write (f"Winner:{winner}")
    fileoutput.write("\n")
    fileoutput.write ("----------------------------")