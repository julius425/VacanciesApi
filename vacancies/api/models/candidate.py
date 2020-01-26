from django.db import models
from django.utils.text import slugify


class Candidate(models.Model):
    
    vacancy = models.ForeignKey(
        'Vacancy',
        related_name='candidate',
        on_delete=models.CASCADE,
    )

    candidate_id = models.IntegerField(default=0)