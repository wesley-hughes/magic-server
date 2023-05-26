"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from magicmenuapi.models import Recipe
from magicmenuapi.serializers import RecipeSerializer


class RecipeView(ViewSet):
    """MM Recipe view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single recipe

        Returns:
            Response -- JSON serialized recipe
        """
        try:
            recipe = Recipe.objects.get(pk=pk)
            serializer = RecipeSerializer(recipe)
            return Response(serializer.data)
        except Recipe.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all recipes

        Returns:
            Response -- JSON serialized list of recipes
        """
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    