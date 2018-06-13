from django.db import models
from django.contrib.auth.models import User as DjangoUser

# PERIODS = (
#     ('MORNING', 'Manhã'),
#     ('AFTERNOON', 'Tarde'),
#     ('BOTH', 'Integral'),
# )


class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

    def __str__(self):
        return self.user.get_full_name()


class Student(User):
    # availability = models.CharField('disponibilidade', max_length=10, choices=PERIODS)
    class Meta:
        verbose_name = 'estudante'
        verbose_name_plural = 'estudantes'

    def __str__(self):
        return self.user.get_full_name()


class Company(User):
    class Meta:
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'

    def __str__(self):
        return self.user.get_full_name()


# class Jobs(models.Model):
#     period = models.CharField('período', max_length=10, choices=PERIODS)

