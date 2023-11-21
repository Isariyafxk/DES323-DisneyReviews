from django.db import models

# Create your models here.
class DisneylandReview(models.Model):
    review_id = models.CharField(max_length=10000)
    rating = models.IntegerField()
    text = models.CharField(max_length=1000)
    branch = models.CharField(max_length=255)