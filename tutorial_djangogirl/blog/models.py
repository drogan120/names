from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(blank=True, editable=False)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
class Comment(models.Model):
    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def save(self):
        self.created_date = timezone.now()
        super(Comment, self).save()
    
    def __str__(self):
        return self.text

class Tag(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Tag_link(models.Model):
    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE)
    tag = models.ForeignKey('blog.Tag', on_delete=models.CASCADE)
