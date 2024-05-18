from django.db import models
from django.contrib.auth.models import User

class Write(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    content = models.TextField()
    create_date = models.DateTimeField()

class Friend(models.Model) :
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_friend_requests')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_friend_requests')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', '신청중'), ('accepted', '수락됨'), ('rejected', '거절됨')], default='신청중')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', symmetrical=True, blank=True)

    def __str__(self):
        return self.user.username