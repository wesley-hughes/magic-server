from django.db import models


class Menu(models.Model):
    user = models.ForeignKey('mmuser', on_delete=models.CASCADE, related_name='menus')
    date = models.DateField()
    sunday_recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='sunday_menus')
    monday_recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='monday_menus')
    tuesday_recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='tuesday_menus')
    wednesday_recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='wednesday_menus')
    thursday_recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='thursday_menus')
    friday_recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='friday_menus')
    saturday_recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='saturday_menus')

