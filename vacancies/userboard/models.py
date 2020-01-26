from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify 
from django.contrib.auth.models import User
from django.shortcuts import reverse 


class Profile(models.Model):
    """
    Модель профиля пользователя.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    slug = models.SlugField(
        null=True,
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}\'s profile.'.format(self.user.username)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs) 

    def get_absolute_url(self):
        return reverse('userboard:profile', kwargs={'slug':self.slug})

    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Для автоматического создания профиля при регистрации пользователя 
    """
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


post_save.connect(create_profile, sender=User)