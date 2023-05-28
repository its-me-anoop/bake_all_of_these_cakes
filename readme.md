# Bake all of these cakes

This is a Python script that calculates which cakes can be baked based on a list of recipes and the available ingredients. This program is helpful for bakers who want to make the most out of their current stock of ingredients.

## Function

`cakes(recipe_list, available)`

The function takes two arguments:

- `recipe_list`: A list of dictionaries, where each dictionary represents a cake recipe. Each dictionary has a 'name' key (the name of the cake), and an 'ingredients' key (a dictionary of ingredients required for that cake, where the keys are the ingredient names and the values are the quantities required).
- `available`: A dictionary where keys represent ingredients and values represent the amount of each ingredient that is available.

The function returns a list of cake names that can be baked given the available ingredients. If no cake can be baked, the function returns an empty list.

```python
recipe_list = [
    {"name": "Pound Cake", "ingredients": {"flour": 500, "sugar": 200, "eggs": 1}},
    {"name": "Vanilla Cake", "ingredients": {"flour": 500, "sugar": 200, "eggs": 1, "vanilla": 2}}
]
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe_list, available))
