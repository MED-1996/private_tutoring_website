from django.db import models
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):
    subject_name = models.CharField(max_length=200, unique=True)
    
    def __str__(self) -> str:
        return f'{self.subject_name}'


class Client(models.Model):
    
    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR', _('Freshman - (9th Grade)')
        SOPHOMORE = 'SO', _('Sophomore - (10th Grade)')
        JUNIOR = 'JR', _('Junior - (11th Grade)')
        SENIOR = 'SR', _('Senior - (12th Grade)')
        COLLEGE = 'GR', _('University')

    name = models.CharField(max_length=150, verbose_name='Students Full Name')
    email = models.EmailField(max_length=254)
    grade_level = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.JUNIOR,
        verbose_name='Grade Level'
    )
    subject = models.ForeignKey(
        Subject,
        to_field='subject_name',
        on_delete=models.SET_NULL,
        related_name= 'subject',
        null=True,
        verbose_name='Subject',
    )
    comment = models.TextField(max_length=1500, blank=True, null=True, verbose_name='Additional Information')
    creation_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}: {self.grade_level} - {self.subject}'
