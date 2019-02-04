import operator

users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

friends = { 'Hero': 2, 'Dunn': 3, 'Sue': 3, 'Chi':3, 'Thor':2, 'Clive':2, 'Hicks': 3, 'Devin':2, 'Kate':3, 'Klein': 1}

#number of friends for a user

def num_friends(user):
    

    for user in friends:
        print(user, 'has %s' % friends.get(user), 'friends')
        
num_friends(users)


#sorting users by number of friends

def sort_by_num_friends(user):
    
    print("\nsorting from most to least number of friends\n")
    
    sorted_list = sorted(friends.items(), key=operator.itemgetter(1), reverse = True)
    for key,value in sorted_list:
        print(key, "has", value, "friends")
   

    
sort_by_num_friends(users)
