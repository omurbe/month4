from django.db import models

# Create your models here.


class TagCloth(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cloth(models.Model):
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(TagCloth, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    cloth = models.ForeignKey(Cloth,
                             related_name='reviews',
                             on_delete=models.CASCADE)
    stars = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.cloth.name}"