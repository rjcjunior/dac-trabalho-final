from django.db import models
from django.contrib.auth.models import User as DjangoUser

PERIOD_MORNING = 'MORNING'
PERIOD_AFTERNOON = 'AFTERNOON'
PERIOD_BOTH = 'BOTH'

PERIOD_LIST = (
    (PERIOD_MORNING, 'Manhã'),
    (PERIOD_AFTERNOON, 'Tarde'),
    (PERIOD_BOTH, 'Integral'),
)

STATUS_REJECTED = 'REJECTED'
STATUS_PENDING = 'PENDING'
STATUS_AVAILABLE = 'AVAILABLE'
STATUS_CLOSED = 'CLOSED'

STATUS_LIST = (
    (STATUS_REJECTED, 'Rejeitado'),
    (STATUS_PENDING, 'Pendente'),
    (STATUS_AVAILABLE, 'Disponível'),
    (STATUS_CLOSED, 'Encerrado'),
)


class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

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
    title = models.CharField(max_length=80, verbose_name='Título')
    description = models.CharField(max_length=1024, verbose_name='Descrição')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa')
    status = models.CharField(max_length=10, choices=STATUS_LIST, verbose_name='Status')
    period = models.CharField(max_length=10, choices=PERIOD_LIST, verbose_name='Período')
    application_date = models.DateField(verbose_name='Prazo de Inscrição', auto_now_add=True)
    response_date = models.DateField(verbose_name='Data de Resposta', auto_now_add=True)

    class Meta:
        verbose_name = 'estagio'
        verbose_name_plural = 'estagios'

    def __str__(self):  # Mostra o nome de cada Speaker no admin
        return self.title


