print('*** Election ***')
numVote = map(int,input('Enter a number of voter(s) : '))
Voter = input('').split()

correctVote = []
falseVote = []

for i in Voter:
    if int(i) > 0 and int(i) <= 20:
        correctVote.append(i)
    else:
        falseVote.append(i)

set(correctVote)

if len(falseVote) > 0:
    print('*** No Candidate Wins ***')
else:
    print(max(set(correctVote)))