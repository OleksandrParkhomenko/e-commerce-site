from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    def profile_picture_filename(self, filename):
        folder = "profile_pictures/"
        username = self.user.username
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extension = filename.split('.')[-1]
        return "{}profile-picture-{}-{}.{}".format(folder, username, time, extension)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default/profile-picture.png', upload_to=profile_picture_filename)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
