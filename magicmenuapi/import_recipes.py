import json
from magicmenuapi.models import Recipe

# Load the JSON data from your database
with open('database.json') as json_file:
    data = json.load(json_file)

# Get the recipe objects from the "recipes" key in the JSON
recipe_objects = data['recipes']

# Iterate over each recipe object
for recipe_obj in recipe_objects:
    # Extract the desired information from the recipe object
    recipe = Recipe(
        title=recipe_obj['title'],
        vegetarian=recipe_obj['vegetarian'],
        vegan=recipe_obj['vegan'],
        gluten_free=recipe_obj['glutenFree'],
        dairy_free=recipe_obj['dairyFree'],
        extended_ingredients=[ingredient['original'] for ingredient in recipe_obj['extendedIngredients']],
        recipe_id=recipe_obj['id'],
        ready_in_minutes=recipe_obj['readyInMinutes'],
        image=recipe_obj['image'],
        dish_types=recipe_obj['dishTypes'],
        instructions=recipe_obj['instructions']
    )

    # Save the recipe to the database
    recipe.save()
