def cakes(recipe_list, available):
    """
    Calculate the cakes that can be baked based on a list of recipes and available ingredients.
    
    The function considers if there's a sufficient quantity of each ingredient for each recipe 
    and excludes those ingredients which are required in zero quantity.
    
    Args:
    recipe_list (list): A list of dictionaries with each dictionary having a 'name' key 
                        representing the cake's name and 'ingredients' key with another 
                        dictionary as its value, which has ingredients as keys and amounts 
                        required for one cake as values.
    available (dict): A dictionary with ingredients as keys and amounts available as values.
    
    Returns:
    list: The names of the cakes that can be baked given the available ingredients. 
          If no cake can be baked, returns an empty list.
    
    Example:
    >>> recipe_list = [{"name": "Pound Cake", "ingredients": {"flour": 500, "sugar": 200, "eggs": 1}},
                        {"name": "Vanilla Cake", "ingredients": {"flour": 500, "sugar": 200, "eggs": 1, "vanilla": 2}}]
    >>> available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    >>> cakes(recipe_list, available)
    ["Pound Cake"]
    """
    can_make = []
    for recipe in recipe_list:
        ingredients_needed = recipe["ingredients"]
        number_of_cakes = []
        for ingredient in ingredients_needed:
            if ingredients_needed[ingredient] == 0:
                continue
            if ingredient in available:
                cakes_from_ingredient = available[ingredient] // ingredients_needed[ingredient]
                number_of_cakes.append(cakes_from_ingredient)
            else:
                break
        else:  # this else corresponds to the for-loop, it executes when the loop finishes normally, i.e., not by a break
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
