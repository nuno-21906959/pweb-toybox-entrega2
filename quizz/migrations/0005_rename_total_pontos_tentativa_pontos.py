# Generated by Django 3.2.3 on 2021-06-01 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0004_auto_20210601_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tentativa',
            old_name='total_pontos',
            new_name='pontos',
        ),
    ]