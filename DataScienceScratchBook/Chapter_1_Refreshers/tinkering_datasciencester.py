# Dump of users working in Datasciencester
datasciencester_dump = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Ram"},
    {"id": 4, "name": "Thorson"},
    {"id": 5, "name": "CliveKent"},
    {"id": 6, "name": "HicksNoze"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Charles"},
]

# list of friendship pairs among the users in the DataSciencester
datasciencester_friendship_data = [
    (0, 1),  # User 0 is in friendship with User 1
    (0, 2),  # User 0 is in friendship with User 2
    (1, 2),  # User 1 is in friendship with User 2
    (1, 3),  # User 1 is in friendship with User 3
    (2, 3),  # User 2 is in friendship with User 3
    (3, 4),  # User 3 is in friendship with User 4
    (4, 5),  # User 4 is in friendship with User 5
    (5, 6),  # User 5 is in friendship with User 6
    (5, 7),  # User 5 is in friendship with User 7
    (6, 8),  # User 6 is in friendship with User 8
    (7, 8),  # User 7 is in friendship with User 8
    (8, 9),  # User 8 is in friendship with User 9
]

user_friendships = {}
# List of user ids with their friends
# create a empty dictionary with id as keys
user_friendships = {user["id"]: [] for user in datasciencester_dump}


def return_friends(user_id):
    for id, friends in user_friendships.items():
        if id == user_id:
            return friends


# iterate through all the friendship data and create a dictionary out of it
for i, j in datasciencester_friendship_data:
    user_friendships[i].append(j)
    user_friendships[j].append(i)

# find average number of connections
total_connections = 0
for k, v in user_friendships.items():
    total_connections += len(v)

print(f"Average connections are: {total_connections/len(user_friendships)}")

# Most connected user
most_connected_user = 0
most_connections = 0
for k, v in user_friendships.items():
    if most_connections < len(v):
        most_connections = len(v)
        most_connected_user = k

# The above example is of degree centrality
print(
    f"Most connected user is: {most_connected_user} with total connections: {most_connections}"
)

# Finding the friends of friends
fof = []
for k, v in user_friendships.items():
    for f in v:
        fof.extend([uf for uf in user_friendships[f] if uf in v])

    print(f"{k}'s friend of friends are: {set(fof)}")
    fof = []

# Data about users and their interests
user_interests = [
    (0, "Hadoop"),
    (0, "Big Data"),
    (0, "HBase"),
    (0, "Java"),
    (0, "Spark"),
    (0, "Cassandra"),
    (0, "Storm"),
    (1, "NoSQL"),
    (1, "MongoDB"),
    (1, "Cassandra"),
    (1, "HBase"),
    (1, "Postgres"),
    (2, "Python"),
    (2, "Scikit-Learn"),
    (2, "Scipy"),
    (2, "Numpy"),
    (2, "Statsmodels"),
    (2, "Pandas"),
    (3, "R"),
    (3, "Python"),
    (3, "Statistics"),
    (3, "Regression"),
    (3, "probability"),
    (4, "machine learning"),
    (4, "regression"),
    (4, "decision trees"),
    (4, "libsvm"),
    (5, "Python"),
    (5, "R"),
    (5, "Java"),
    (5, "C++"),
    (5, "Haskell"),
    (5, "programming languages"),
    (6, "statistics"),
    (6, "probability"),
    (6, "mathematics"),
    (6, "theory"),
    (7, "machine learning"),
    (7, "scikit-learn"),
    (7, "Mahout"),
    (7, "neural networks"),
    (8, "neural networks"),
    (8, "deep learning"),
    (8, "Big Data"),
    (8, "artificial intelligence"),
    (9, "Hadoop"),
    (9, "Java"),
    (9, "MapReduce"),
    (9, "Big Data"),
]

# find users with common interests
common_user_intersts = {user_interest[1]: [] for user_interest in user_interests}
for user_interest in user_interests:
    common_user_intersts[user_interest[1]].append(user_interest[0])

print("List of common user interests:\n", common_user_intersts)

# create a dictionary for users and their interests
user_interest_dict = {
    user_interest[0]: [
        interest[1] for interest in user_interests if interest[0] == user_interest[0]
    ]
    for user_interest in user_interests
}

print("List of interests:\n", user_interest_dict)

# Salaries and Experience
salaries_and_tenures = [
    (83000, 8.7),
    (88000, 8.1),
    (48000, 0.7),
    (76000, 6),
    (69000, 6.5),
    (76000, 7.5),
    (60000, 2.5),
    (83000, 10),
    (48000, 1.9),
    (63000, 4.2),
]
print(
    f"The maximum salary is {max(salaries_and_tenures)[0]} with y.o.e as {max(salaries_and_tenures)[1]}"
)

# Bucket the yoe with salaries
bucket_salaries_and_tenures = {
    "0-3": 0,
    "3-6": 0,
    "6-10": 0,
}
for st in salaries_and_tenures:
    if st[1] <= 3:
        bucket_salaries_and_tenures["0-3"] += st[0]
    elif st[1] > 3 and st[1] <= 6:
        bucket_salaries_and_tenures["3-6"] += st[0]
    else:
        bucket_salaries_and_tenures["6-10"] += st[0]

print(bucket_salaries_and_tenures)
