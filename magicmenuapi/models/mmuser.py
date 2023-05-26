from django.db import models
from django.contrib.auth.models import User

class MMUser(models.Model):
    # Relationship to the built-in User model which has name and email
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    dairy_free = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
