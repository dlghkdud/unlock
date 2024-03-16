from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Write(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.author