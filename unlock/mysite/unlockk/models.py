from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Write(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    content = models.TextField()
    create_date = models.DateTimeField()

class Friend(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='pending')  # 'pending', 'accepted', 'rejected'
    
    def __str__(self):
        return f"{self.from_user} to {self.to_user} - {self.status}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', symmetrical=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 변경된 부분
    profile_photo = models.ImageField(blank=True)
