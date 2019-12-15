from __future__ import division


# GOAL => Verify users relations

# A small list of users - "dict"
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

# Friend pairs related - an array of tuples
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Initialize a new dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}
print("Friendships", friendships)

# Populating the friendship list for each user
for i, j in friendship_pairs:
  # print(i, j)
  # iterate over the list
  friendships[i].append(j) # add j as a friend of i
  friendships[j].append(i) # add i as a friend of j
print("Friendships with friends connections", friendships)

# First question: "what is the average number of connections?"
# Steps:
# 1 - Find the total number of connections
# 2 - Then, divide by the number of users

# Calculate the total number of connections as a function
def number_of_friends(user):
  """how many friends does the user have ? """
  user_id = user["id"]
  friends_ids = friendships[user_id]
  return len(friends_ids) # the list length

# Calculate the total connection looping over the users
total_connections = sum(number_of_friends(user) for user in users)
# Printing out the total connections number
print("Total connections", total_connections)

# Checking confidence
assert total_connections == 24


# Calculating the average number of connections
# Number of users
num_users = len(users)
# Average connections
avg_connections = total_connections / num_users
print("Avg connections", avg_connections)

# Checking confidence
assert num_users == 10
assert avg_connections == 2.4

# Also, find the people more connected
# Sort from largest to smallest

# Create a list (user_id, number_of_friends)
number_of_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
# Printing out the number of friends
# Each pair is (user_id, num_friends):
print("Number of friends", number_of_friends_by_id)

# Sort friends
number_of_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)
print("Number of friends sorted", number_of_friends_by_id)

# Checking confidence
assert number_of_friends_by_id[0][1] == 3 # several people have 3 friends
assert number_of_friends_by_id[-1] == (9, 1) # user 9 has only 1 friend

# These bunch of code above were important to compute
# a metric network of degree of centrality
# PT-BR: uma rede métrica de grau de centralidade
# e pode ser representada por uma rede grafos determinando
# suas conexões

# GOAL => Estimulate more connection between the members
# So, develop suggestion of "data scientists you may know"