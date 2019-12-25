from django import forms

from .models import Article, Comment

class DateInput(forms.DateInput):
    input_type = 'date'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }

class ArticleForm(forms.ModelForm):
    tagsChoice = [
        ('HTML', 'HTML'),
        ('Python', 'Python'),
        ('PHP', 'PHP'),
        ('Javascript', 'Javascript'),
    ]

    tags = forms.MultipleChoiceField(
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control tags'}),
        choices=tagsChoice,
    )

    class Meta:
        model = Article
        fields = ['title', 'text', 'published_date']
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'text': forms.Textarea(attrs = {'class': 'form-control'}),
            'published_date': DateInput(attrs = {'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')

        if title == 'print':
            self.add_error('title', 'cant use the string print.')
    