
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
