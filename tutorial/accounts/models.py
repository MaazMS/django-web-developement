from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='pune')


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone  = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

    pune = UserProfileManager()
def create_profile(sender, **kwargs):
    if kwargs['created']:
        Users_Profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


