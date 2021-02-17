from django.db import models

#constants
from accounts.models import User
from post.models import Post

MAX_LENGTH = 100


class Comment(models.Model):

    title = models.CharField('Title', max_length=MAX_LENGTH)

    content = models.TextField('Comment')

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    post = models.ForeignKey(Post, on_delete= models.CASCADE, verbose_name='Post')


    def __str__(self):

        return f'Comment by {self.author} on {self.updated_at.date()}'
