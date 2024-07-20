from django.db import models
from django.contrib.auth.models import User
from PIL import Image  #pillow lib


class Profile(models.Model):
  #OneToOneField == user has only one profile
  user = models.OneToOneField( 
    User,
    on_delete=models.CASCADE
  )

  avatar = models.ImageField(
    default='default.jpg',
    upload_to='profile_avatar'
  )

  def __str__(self):
    return f'{self.user.username} Profile'

  def save(self, *args, **kwargs): #save profile infos
    super().save(*args, **kwargs) 
    img = Image.open(self.avatar.path)
    if img.height > 300 or img.width > 300:
      output_size = (300, 300)
      img.thumbnail(output_size)
      img.save(self.avatar.path)
      