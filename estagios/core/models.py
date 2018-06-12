from django.db import models
from django.contrib.auth.models import User

# PERIODS = (
#     ('MORNING', 'Manhã'),
#     ('AFTERNOON', 'Tarde'),
#     ('BOTH', 'Integral'),
# )


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # availability = models.CharField('disponibilidade', max_length=10, choices=PERIODS)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# class Jobs(models.Model):
#     period = models.CharField('período', max_length=10, choices=PERIODS)

