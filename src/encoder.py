import numpy as np

def build_ingredient_index(corpus):
    """
    Creates a dictionary mapping each ingredient to an index.
    """
    ingredient_index = {}
    idx = 0
    for ingredients in corpus:
        for ingredient in ingredients:
            if ingredient not in ingredient_index:
                ingredient_index[ingredient] = idx
                idx += 1
    return ingredient_index


def one_hot_encode(ingredients, ingredient_index):
    """
    Converts a list of ingredients into a one-hot encoded vector.
    """
    vector = np.zeros(len(ingredient_index))
    for ingredient in ingredients:
        if ingredient in ingredient_index:
            vector[ingredient_index[ingredient]] = 1
    return vector
