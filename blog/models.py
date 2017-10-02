from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Feedback(models.Model):
    '''Save Feedback from user'''
    title = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User')
    time = models.DateTimeField(default=timezone.now)
    message = models.CharField(max_length=1000)

    def __str__(self):
        ''' Object representation'''
        return self.title

