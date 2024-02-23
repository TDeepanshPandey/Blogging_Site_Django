from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    """
    A form for creating a new blog post.
    
    Attributes:
        title (CharField): A field representing the title of the post.
        text (TextField): A field representing the content of the post.
    """
    
    class Meta:
        model = Post
        fields = ('author','title', 'text',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
    
    

class CommentForm(forms.ModelForm):
    """
    A form for creating a new comment on a blog post.
    
    Attributes:
        author (CharField): A field representing the name of the author of the comment.
        text (TextField): A field representing the content of the comment.
    """
    
    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }