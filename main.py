import os
import csv

votes_cast=[]
county=[]
candidates=[]
names=['Khan:','Correy:','Li:',"O'Tooley:"]

csvpath=os.path.join('..','..','RICEHOU201906DATA1','HW','03-Python','Instructions','Pypoll','Resources','election_data.csv')
                    
with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    for rows in csvreader:
        votes_cast.append(rows[0])
        county.append(rows[1])
        candidates.append(rows[2])

    print('Election Results')
    print('--------------------------')
    print('Total Votes: '+str(len(votes_cast[1:])))
    print('--------------------------')
    
    khan_votes=candidates.count('Khan')
    correy_votes=candidates.count('Correy')
    li_votes=candidates.count('Li')
    otooley_votes=candidates.count("O'Tooley")
    
    khan_average =(khan_votes/(correy_votes+li_votes+otooley_votes+khan_votes)*100)
    correy_average=(correy_votes/(khan_votes+correy_votes+li_votes+otooley_votes)*100)
    li_average=(li_votes/(khan_votes+correy_votes+li_votes+otooley_votes)*100)
    otooley_average=(otooley_votes/(khan_votes+correy_votes+li_votes+otooley_votes)*100)

    khan_average_decimal=round(khan_average,4)
    correy_average_decimal=round(correy_average,4)
    li_average_decimal=round(li_average,4)
    otooley_votes_decimal=round(otooley_average,4)

    print(names[0]+' '+ str(khan_average_decimal)+'%'+' '+'('+str(khan_votes)+")")
    print(names[1]+' '+ str(correy_average_decimal)+'%'+" "+'('+ str(correy_votes)+")")
    print(names[2]+' '+ str(li_average_decimal)+'%'+' '+'('+ str(li_votes)+')')
    print(names[3]+' '+ str(otooley_votes_decimal)+'%'+" "+"("+ str(otooley_votes)+')')

    print('--------------------------')

    winner = {'Khan':khan_votes,"Correy":correy_votes,'Li':li_votes,"O'Tooley":otooley_votes}

    print('Winner: '+str(max(winner, key=winner.get)))

    print('--------------------------')

        
  