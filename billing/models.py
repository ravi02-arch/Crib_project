from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Items(models.Model):
    name = models.CharField(max_length=20)
    amount = models.IntegerField(default=0)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
