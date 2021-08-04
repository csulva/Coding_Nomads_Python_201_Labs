# ingredients.py
from recipes.soup import make_soup
def prepare(ingredient):
    print(f"You cooked the {ingredient}.")
    return f"cooked {ingredient}"

carrot = "carrot"
salt = "salt"
potato = "potato"
broth = 'broth'

if __name__ == "__main__":
    print(prepare(potato))

