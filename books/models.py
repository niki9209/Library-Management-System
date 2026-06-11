from django.db import models

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title