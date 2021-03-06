# Generated by Django 2.0.6 on 2018-07-08 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='application_date',
            field=models.DateField(auto_now_add=True, verbose_name='Prazo de Inscrição'),
        ),
    ]
