print('*** Election ***')
elect = int(input('Enter a number of voter(s) : '))
voters = input('').split()
vote = []
negativeVote = []

for x in voters:
    if(int(x) > 0 and int(x) <= 20):
        vote.append(int(x))    


if(len(vote) < 1 or (len(negativeVote) > 0)):
    print('*** No Candidate Wins ***')
elif(len(vote) > 0):
    print(max(set(vote), key=vote.count))

