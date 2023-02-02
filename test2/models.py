from django.db import models
from test1.models import Post

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts') 
    comment = models.TextField() 

    def __str__(self) -> str:
        return f'{self.post} коментарий к посту -- {self.comment}'




