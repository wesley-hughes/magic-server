from django.db import models


class Favorite(models.Model):
    user = models.ForeignKey('mmuser', on_delete=models.CASCADE, related_name='favorites')
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
