from django.contrib import admin
from .models import Article, Tag, Tag_link, Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

admin.site.register(Tag)
admin.site.register(Tag_link)
admin.site.register(Comment)
admin.site.register(Article, ArticleAdmin)