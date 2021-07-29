# Write a function that prints out nicely formatted information about a
# real estate listing. The information can vary for every listing, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.
import pprint
def listing(**kwargs):
    return list(kwargs.items())


print(listing(price=400000, stories=2, baths=3, rooms=5, furniture=None, neighbors=None, acres=40))