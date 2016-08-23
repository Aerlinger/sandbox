db = {
    "A": ["B", "C", "D"],
    "B": ["A", "C", "D", "E"],
    "C": ["A", "B", "D", "E"],
    "D": ["A", "B", "C", "E"],
    "E": ["B", "C", "D"]
}


def map(group):
    associations = {}
    for individual in group:
        individual_friends = group[individual]
        for friend in individual_friends:
            friend_pairs = (individual, friend)
            associations.update( {friend_pairs: individual_friends} )

    print str(associations).replace("],", "]\n")

    # Merge matching keys:



def reduce(map):


map(db)