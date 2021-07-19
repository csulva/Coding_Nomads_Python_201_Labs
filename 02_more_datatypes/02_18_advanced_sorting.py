# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!

movie_ratings = {}
movie_ratings['Lotr'] = 10
movie_ratings['Avengers: Infinity War'] = 8
movie_ratings['Harry Potter'] = 7
movie_ratings['Indiana Jones'] = 6

movie_ratings = sorted(movie_ratings.items())

movie_ratings = tuple(movie_ratings)
print(movie_ratings)