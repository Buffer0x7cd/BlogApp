from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    ''' Posts in blog'''
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

class Comment(models.Model):
    '''Save comments on blog posts'''
    post = models.ForeignKey(Post, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
