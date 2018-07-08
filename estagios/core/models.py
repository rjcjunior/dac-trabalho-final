from django.db import models
from django.contrib.auth.models import User as DjangoUser

PERIOD_LIST = (
    ('MORNING', 'Manhã'),
    ('AFTERNOON', 'Tarde'),
    ('BOTH', 'Integral'),
)

STATUS_LIST = (
    ('REJECTED', 'Rejeitado'),
    ('PENDING', 'Pendente'),
    ('AVAILABLE', 'Disponível'),
    ('CLOSED', 'Encerrado'),
)


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
    company_name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)

    class Meta:
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'

    def __str__(self):
        return self.company_name


class Job(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=1024)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=STATUS_LIST)
