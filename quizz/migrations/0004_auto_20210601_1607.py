# Generated by Django 3.2.3 on 2021-06-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0003_alter_tentativa_pontuacao_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tentativa',
            name='pontuacao_total',
        ),
        migrations.AddField(
            model_name='tentativa',
            name='total_pontos',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
