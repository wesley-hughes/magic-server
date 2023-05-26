from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    dairy_free = models.BooleanField(default=False)
    extended_ingredients = models.JSONField(default=list)
    recipe_id = models.IntegerField(unique=True)
    ready_in_minutes = models.IntegerField()
    image = models.URLField(max_length=255)
    dish_types = models.JSONField(default=list)
    instructions = models.TextField()


