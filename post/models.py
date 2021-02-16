from django.db import models


#constants
from topic.models import Topic

MAX_LENGTH = 100

class Post(models.Model):

    """
        This class implements Post ORM
    """

    title = models.CharField('Title' ,max_length= MAX_LENGTH)

    content = models.TextField('Body')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Topic')
