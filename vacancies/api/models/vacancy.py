from django.db import models
from django.utils.text import slugify
from userboard.models import User
from django.shortcuts import reverse 


class Vacancy(models.Model):
    
    STATES = (
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE'),
        ('ARCHIVE', 'ARCHIVE'),
    )

    title = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    state = models.CharField(
        max_length=50,
        choices=STATES
    )

    owner = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='vacancy',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("userboard:vacancy_detail", kwargs={"pk": self.pk})


    @classmethod
    def filter_by_state(cls, state):
        return cls.objects.filter(state=state)

    @classmethod
    def get_all_states(cls):
        return cls.objects.all().values_list('state', flat=True).distinct()

    @classmethod
    def filter_by_owner(cls, username):
        user_pk = User.objects.get(username=username).pk
        owner = User.objects.get(pk=user_pk)
        return cls.objects.filter(owner=owner).exclude(state='ARCHIVE')

    @classmethod
    def filter_non_archived(cls):
        return cls.objects.exclude(state='ARCHIVE')
    
    @classmethod
    def filter_archived(cls):
        return cls.objects.filter(state='ARCHIVE')

    @classmethod
    def get_user_vacancies(cls, user):
        return cls.objects.filter(owner=user)