import os
import csv
total_votes= 0
candidate_data = []
candidate_names=[]
unique_names=[]
results=[]


file=os.path.join('election_data.csv')
with open (file,newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for x in csvreader:

        candidate_data.append(x)
        total_votes+= 1

for y in candidate_data:
    candidate_names.append(y[2])

for z in candidate_names:    
    if z not in unique_names:
        unique_names.append(z)

for b in range(len(unique_names)):
    results.append(candidate_names.count(unique_names[b]))

winner=unique_names[results.index(max(results))]

print (f'   Election Results\n\n--------------------\n\n Total Votes : {total_votes} \n\n--------------------\n\n') 

for d in range(len(unique_names)):
    print (f'{unique_names[d]} : {round((results[d]/total_votes)*100,3)}% ({results[d]}) \n')

print (f'\n--------------------\n Winner : {winner}\n--------------------')

text_file=open("Analysis.txt",'w')
text_file.write(f'   Election Results\n\n--------------------\n\n Total Votes : {total_votes} \n\n--------------------\n\n')
for d in range(len(unique_names)):
    text_file.write (f'{unique_names[d]} : {round((results[d]/total_votes)*100,3)}% ({results[d]}) \n')
text_file.write(f'\n--------------------\n Winner : {winner}\n--------------------')
