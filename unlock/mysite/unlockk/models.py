from django.db import models
from django.contrib.auth.models import User

class Write(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    content = models.TextField()
    create_date = models.DateTimeField()

class Follow(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user")
    to_user = models.ManyToManyField(User,related_name="to_user")