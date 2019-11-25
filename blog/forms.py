from django import forms

from .models import Post, Comment, Category

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    favorite_fruit = forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))
    

    def clean_your_name(self):
        data = self.cleaned_data['your_name']
        print(data)
        if not data.islower():
           raise forms.ValidationError("Usernames should be in lowercase")
        if 'a' in data:
           raise forms.ValidationError("Usernames should not contain a.")
        return data

class Categoryform(forms.ModelForm):

    categories = (
        ('1', 'red'),
        ('2', 'blue'),
        ('3', 'black')
    )
    category = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple,
    choices=categories)


