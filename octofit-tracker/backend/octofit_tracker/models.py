from djongo import models
from djongo.models import ObjectIdField

class User(models.Model):
    _id = ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Team(models.Model):
    _id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)

class Activity(models.Model):
    _id = ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='_id')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    _id = ObjectIdField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, to_field='_id')
    points = models.IntegerField()

class Workout(models.Model):
    _id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
