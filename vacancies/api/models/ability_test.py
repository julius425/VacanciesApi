from django.db import models
from django.utils.text import slugify
from userboard.models import User
from django.shortcuts import reverse 



class AbilityTest(models.Model):
    vacancy = models.ForeignKey(
        'Vacancy',
        blank=True,
        null=True,
        related_name='ability',
        on_delete=models.CASCADE
    )

    slug = models.SlugField(
        null=False,
        blank=True,
    )

    title = models.CharField(
        max_length=250
    )
    
    is_active = models.BooleanField(
        default=True
    )

    description = models.TextField(
        blank=True,
    )

    ab_test = models.FileField(blank=True,
    )

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.slug)

        return super().save(*args, **kwargs) 

    def get_file_url(self):
        name = self.ab_test.name 
        return reverse('userboard:download', kwargs={'file_name':self.ab_test.name})
   
     