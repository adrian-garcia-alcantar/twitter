from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    head_shot = models.ImageField(upload_to='head_shots', default='head_shots/User.png')
    birth_date = models.DateField()
    location = models.CharField(max_length=50, blank=True, null=True)


class Tweet(models.Model):
    owner = models.ForeignKey("Profile", related_name='tweet')
    status = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
