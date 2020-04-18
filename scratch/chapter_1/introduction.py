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

print("----------------------------------------")


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

print("----------------------------------------")

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

print("----------------------------------------")

# Also, find the people more connected
# Sort from largest to smallest

# Create a list (user_id, number_of_friends) as tuples
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

print("----------------------------------------")

# These bunch of code above were important to compute
# a metric network of degree of centrality
# PT-BR: uma rede metrica de grau de centralidade
# e pode ser representada por uma rede grafos determinando
# suas conexoes

# GOAL => Estimulate more connection between the members
# So, develop suggestions of "data scientists you may know"

# First instict is suggest an user may know friends of friends

# A function to iterate over a friend of users, iterate over
# friends of that person
def foaf_ids_bad(user):
    """foaf is short for "friend of a friend" """
    return [foaf_id
            for friend_id in friendships[user["id"]] # for each friend of a user
            for foaf_id in friendships[friend_id]] # take their friends

[0, 2, 3, 0, 1, 3] # result for user[0]

print('user[0]', users[0])
print('foaf to user[0]', foaf_ids_bad(users[0]))

assert foaf_ids_bad(users[0]) == [0, 2, 3, 0, 1, 3]

print("----------------------------------------")


print("friendships[0]", friendships[0]) # [1, 2]
print("friendships[1]", friendships[1]) # [0, 2, 3]
print("friendships[2]", friendships[2]) # [0, 1, 3]

assert friendships[0] == [1, 2]
assert friendships[1] == [0, 2, 3]
assert friendships[2] == [0, 1, 3]

print("----------------------------------------")


from collections import Counter # não carregador por padrão

def friends_of_friends(user):
  user_id = user["id"]
  return Counter(
    foaf_id
    for friend_id in friendships[user_id]   # For each of my friends
    for foaf_id in friendships[friend_id]   # find their friends
    if foaf_id != user_id                   # who aren't me
    and foaf_id not in friendships[user_id] # and aren't my friends
  )

print(friends_of_friends(users[3]))     # Counter({0: 2, 5: 1})

assert friends_of_friends(users[3]) == Counter({0: 2, 5: 1})

print("----------------------------------------")

# As a Data Scientist, you know you like to find users with
# similar interests "competencia significativa"

print(foaf_ids_bad(users[4]))

# A list of pairs (user_id, interest)
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# Goal => Develop a function to find users with the same interests

def data_scientist_who_like(target_interest):
  """Find the ids of all users who like the target interest."""
  return [user_id
          for user_id, user_interest in interests
          if user_interest == target_interest
        ]

# the function above works, but the entire list must be examined for
# each serch. Could be better build an index of interests for users

from collections import defaultdict

# Keys are interests, values are list of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
  user_ids_by_interest[interest].append(user_id)
  
# Keys are user_ids, values are lists of interests for that user_id.
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
  interests_by_user_id[user_id].append(interest)
  
print("user_ids_by_interest", user_ids_by_interest)

print("----------------------------------------")

print("interests_by_user_id", interests_by_user_id)

print("----------------------------------------")

def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )

print('most common interests with user[1]', most_common_interests_with(users[1]))

print("----------------------------------------")

# Goal => Salaries and Expertise
# Give a list of anonymous salaries and years of experience.

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# The keys are years, values are lists of the salaries for each tenure.
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
  salary_by_tenure[tenure].append(salary)

# The keys are years, each value is average salary for that tenure
average_salary_by_tenure = {
  tenure: sum(salaries) / len(salaries)
  for tenure, salaries in salary_by_tenure.items()
}

assert average_salary_by_tenure == {
    0.7: 48000.0,
    1.9: 48000.0,
    2.5: 60000.0,
    4.2: 63000.0,
    6: 76000.0,
    6.5: 69000.0,
    7.5: 76000.0,
    8.1: 88000.0,
    8.7: 83000.0,
    10: 83000.0
}

print("Average salary by tenure", average_salary_by_tenure)

print("----------------------------------------")

# Function to group cases
def tenure_bucket(tenure):
  if tenure < 2:
    return "less than two"
  elif tenure < 5:
    return "between two and five"
  else:
    return "more than five"

# Keys are tenure buckets, values are list of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

# Grouping salaries by tenure bucket
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# Calculating the salary average by tenure
# Keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {
  tenure_bucket: sum(salaries) / len(salaries)
  for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

print("Average salary by bucket", average_salary_by_bucket)

print("----------------------------------------")

# Goal => Try to predict paid and unpaid accounts
# Missing more data about it

def predict_paid_or_unpaid(years_of_experience):
  if years_of_experience < 3.0:
    return "paid"
  elif years_of_experience < 8.5:
    return "unpaid"
  else:
    return "paid"


# Goal => Planning blog content to the year by interests

# Couting words
words_and_counts = Counter(
  word for user, interest in interests
  for word in interest.lower().split()
)  

# Printing
for word, count in words_and_counts.most_common():
  if count > 1:
    print("Word and count: ", word, count)