from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, null=True, db_index=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(default='default.jpg', upload_to='pics')

    MAX_IMAGE_SIZE = 300

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'
