from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Image(models.Model):
    filepath = models.CharField("Path relative to BASE_PATH for the imafe file", max_length=512)
    caption = models.CharField("Description of the image, where and when it was taken", max_length=250)
    created_date = models.DateTimeField("Data photo was taken")
    file = models.FileField(upload_to=os.path.join(os.path.expanduser('~'), 'Pictures', 'labeler'))

class UserLabel(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User)

class TotalVotes(models.Model):
    name = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)