from django.db import models
from django.conf import settings
from django.utils import timezone


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
class Comment(models.Model):
    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Tag(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Tag_link(models.Model):
    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE)
    tag = models.ForeignKey('blog.Tag', on_delete=models.CASCADE)
