from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField(max_length = 100)
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(null = True)

    def __str__(self):
        return self.title