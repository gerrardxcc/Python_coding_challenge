nominee_1 = input('enter the nominee 1 name: ')
nominee_2 = input('enter the nominee 2 name: ')

nom_1_votes = 0
nom_2_votes = 0

votes_id = [1,2,3,4,5,6,7,8,9,10]

num_of_voter = len(votes_id)

while True:
    if votes_id == []:
        print('voting session over')
        if nom_1_votes > nom_2_votes:
            percent = (nom_1_votes / num_of_voter)*100
            print(nominee_1,'has won','with', percent,'% votes')
            break

        elif nom_2_votes > nom_1_votes:
            percent = (nom_1_votes / num_of_voter)*100
            print(nominee_2,'has won','with', percent,'% votes')
            break

    else:
        voter =  int(input('Please your voter id number: '))
        if voter in votes_id:
            print('you are a voter ')
            votes_id.remove(voter)
            vote = int(input('Please enter your vote number 1 or 2: '))
            if vote == 1:
                nom_1_votes += 1
                print('Thank you for casting your vote')

            elif vote == 2:
                nom_2_votes += 1
                print('Thank you for casting your vote')
        else:
            print("You're not a voter here or you have already voted")
