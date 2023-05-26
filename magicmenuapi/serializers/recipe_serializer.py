from rest_framework import serializers
from magicmenuapi.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title', 'vegetarian', 'vegan', 'gluten_free', 'dairy_free', 'extended_ingredients', 'recipe_id', 'ready_in_minutes', 'image', 'dish_types', 'instructions']



# for reference in case i implement create recipe functionality

# class CreateProductSerializer(serializers.Serializer):
#     categoryId = serializers.IntegerField()
#     name = serializers.CharField()
#     price = serializers.DecimalField(decimal_places=2, max_digits=7)
#     description = serializers.CharField()
#     quantity = serializers.IntegerField()
#     location = serializers.CharField()
#     image = serializers.ImageField()