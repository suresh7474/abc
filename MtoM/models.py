
from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
# publicatin--title and Article-hedline  publications= mtom
class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    # l=models.M

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline