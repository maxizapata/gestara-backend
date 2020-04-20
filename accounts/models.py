from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
# Create your models here.


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User(AbstractUser):
    mobile = models.CharField(max_length=20, blank=True)
    validated_mobile = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos',
                              null=True,
                              blank=True,
                              default='./anonymous-user.png')
    email = models.EmailField(max_length=254, unique=True)

    def is_administrator(self):
        try:
            Administrator.objects.get(pk=self.id)
        except Administrator.DoesNotExist:
            return False
        else:
            return True

    def __str__(self):
        return self.username


class Administrator(models.Model):
    cooperative = models.OneToOneField(User, on_delete=models.DO_NOTHING)
