
from django.db import models

#constants
from accounts.models import User

MAX_LENGTH = 100

class Topic(models.Model):

    """
        This class implements an ORM for the posts
    """
    title = models.CharField('Topic title', max_length=MAX_LENGTH)

    name = models.SlugField("Topic name", max_length=MAX_LENGTH, unique=True)


    author = models.ForeignKey(User, verbose_name='Topic user', on_delete=models.CASCADE)

    description = models.TextField(verbose_name='Topic description')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):

        return self.name