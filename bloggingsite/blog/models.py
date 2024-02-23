from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    """
    A model representing a blog post.

    Attributes:
        author (ForeignKey): A foreign key to the User model representing the author of the post.
        title (CharField): A field representing the title of the post.
        text (TextField): A field representing the content of the post.
        created_date (DateTimeField): A field representing the date and time when the post was created.
        published_date (DateTimeField): A field representing the date and time when the post was published.
    """

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    A model representing a comment on a blog post.

    Attributes:
        post (ForeignKey): A foreign key to the Post model.
        author (CharField): The name of the author of the comment.
        text (TextField): The text of the comment.
        created_date (DateTimeField): The date and time the comment was created.
        approved_comment (BooleanField): Whether the comment has been approved by a moderator.
    """

    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
    
