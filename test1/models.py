from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}  - запостили {self.created_at}'
        