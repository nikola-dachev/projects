from django import forms

from FurryFunnies.posts.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']
        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:',
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Put an attractive and unique title..."
        self.fields['content'].widget.attrs['placeholder'] = "Share some interesting facts about your adorable pets..."


class BasePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']
        labels = {
            'image_url': 'Post Image URL:',
        }
        help_texts = {
            'image_url': ''
        }


class UpdatePostForm(BasePostForm):
    pass

class DeletePostForm(BasePostForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
