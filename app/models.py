from django.db import models

# Create your models here.


class Candidates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    registration = models.IntegerField()


class Voters(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    registration = models.IntegerField()
    vote_king = models.CharField(max_length=255, null=True, blank=True)
    vote_queen = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField()
