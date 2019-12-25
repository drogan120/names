from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, CommentForm
from .models import Article, Tag, Comment
from django.utils import timezone
from django.db.models import Count


def indexView(request):
    articles = Article.objects.all()
    title = request.GET.get('title')
    tag = request.GET.get('tag')
    if title:
        articles = articles.filter(title__contains=title)
    if tag:
        articles = articles.filter(tag__text=tag)
    context = {
        'articles': articles,  
        'tags': Tag.objects.annotate(num_article = Count('article')),
        'colors': ['danger', 'dark', 'success', 'warning', 'primary']
    }
    return render(request, 'blog/index.html', context)


def article_list(request):
    articles = Article.objects.all()
    title = request.GET.get('title')
    tag = request.GET.get('tag')
    if title:
        articles = articles.filter(title__contains=title)
    if tag:
        articles = articles.filter(tag__text=tag)
    context = {
        'articles': articles,  
        'tags': Tag.objects.annotate(num_article = Count('article')),
        'colors': ['danger', 'dark', 'success', 'warning', 'primary']
    }
    return render(request, 'blog/article_list.html', context)

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.all()
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            comment = Comment()
            comment.author = request.user
            comment.article = article
            comment.text = form.cleaned_data['text']
            comment.save()

    context = {
            'article': article,
            'comments': comments,
            'form': form  
        }
    return render(request, 'blog/article_detail.html', context)

def article_new(request):
    form = ArticleForm(request.POST or None)
    tags = Tag.objects.all()

    if request.method == 'POST':
        if form.is_valid():
            article = Article()
            article.author = request.user
            article.title = form.cleaned_data['title']    
            article.text = form.cleaned_data['text']
            article.published_date = form.cleaned_data['published_date']
            tagInput = form.cleaned_data['tags']
            article.save()
            for tag in tagInput:
                article.tag.add(tag)

            return redirect('article_list')
    context = {
        'form': form,
    }
    
    return render(request, 'blog/article_new.html', context) 

def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    tags = Tag.objects.all()

    if form.is_valid():
        article = Article()
        article.author = request.user
        article.title = form.cleaned_data['title']    
        article.text = form.cleaned_data['text']
        article.published_date = form.cleaned_data['published_date']
        article.save()

        return redirect('article_list')
    context = {
        'form': form,
    }
    
    return render(request, 'blog/article_edit.html', context) 

def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

def article_publish(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.publish()
    return redirect('article_list')
    # if request.method == 'POST':
    #     user = request.user
    #     Article.objects.create(
    #         author = user,
    #         title = request.POST.get('title'),
    #         text = request.POST.get('text'),
    #         published_date = timezone.now(),
    #     )
    #     return redirect('dashboard')
    # else:
    #     return render(request, 'blog/article_new.html', {'form': form}) 
