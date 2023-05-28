def cakes(recipe_list, available):
    """
    Calculate the cakes that can be baked based on a list of recipes and available ingredients.

    Args:
    recipe_list (list): A list of dictionaries with each dictionary having a 'name' key representing the cake's name and
                        'ingredients' key with another dictionary as its value, which has ingredients as keys and amounts
                        required for one cake as values.
    available (dict): A dictionary with ingredients as keys and amounts available as values.

    Returns:
    list: The names of the cakes that can be baked given the available ingredients. If no cake can be baked, returns an empty list.

    Example:
    >>> recipe_list = [{"name": "Pound Cake", "ingredients": {"flour": 500, "sugar": 200, "eggs": 1}},
                        {"name": "Vanilla Cake", "ingredients": {"flour": 500, "sugar": 200, "eggs": 1, "vanilla": 2}}]
    >>> available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    >>> cakes(recipe_list, available)
    ["Pound Cake"]
    """
    can_make = []
    for recipe in recipe_list:
        if all(
            ingredient in available and available[ingredient] >= amount
            for ingredient, amount in recipe["ingredients"].items()
        ):
            can_make.append(recipe["name"])
    return can_make


print(
    cakes(
        [
            {
                "name": "Pound Cake",
                "ingredients": {"flour": 500, "sugar": 200, "eggs": 1},
            },
            {
                "name": "Vanilla Cake",
                "ingredients": {"flour": 500, "sugar": 200, "eggs": 1, "vanilla": 2},
            },
            {
                "name": "Apple Cake",
                "ingredients": {"flour": 500, "sugar": 200, "eggs": 1, "apples": 5},
            },
        ],
        {"flour": 1200, "sugar": 1200, "eggs": 5, "vanilla": 200},
    )
)
