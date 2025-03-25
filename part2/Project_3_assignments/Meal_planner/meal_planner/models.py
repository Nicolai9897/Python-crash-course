from django.db import models

# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'ingredients'
        
        
    def __str__(self):
        
        return self.ingredient