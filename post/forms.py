
from django import forms
from django.forms import fields, widgets
from .models import Post

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        


    class Meta:
        model=Post
        fields=['title','description','image']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.author = self.user
        instance = instance.save()
        
        return instance