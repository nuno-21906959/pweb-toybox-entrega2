# Generated by Django 3.2.3 on 2021-06-01 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0005_rename_total_pontos_tentativa_pontos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pergunta',
            name='user',
        ),
    ]
