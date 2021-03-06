from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    img = models.ImageField(default='default.jpg', upload_to="user_image")
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} profile'