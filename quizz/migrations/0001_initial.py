# Generated by Django 3.2.3 on 2021-06-01 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta_text', models.CharField(max_length=900)),
                ('pontos', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontuacao', models.PositiveIntegerField()),
                ('entregue', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quizzes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=200)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('nr_tentativas', models.PositiveIntegerField()),
                ('tempo_limite_mins', models.PositiveIntegerField()),
                ('perguntas', models.ManyToManyField(to='quizz.Pergunta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta_text', models.CharField(max_length=900)),
                ('is_correct', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tentativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.pessoa')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.pergunta')),
                ('quizz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.quizzes')),
                ('resposta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.resposta')),
            ],
        ),
        migrations.AddField(
            model_name='pessoa',
            name='quizz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.quizzes'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pergunta',
            name='resposta',
            field=models.ManyToManyField(to='quizz.Resposta'),
        ),
        migrations.AddField(
            model_name='pergunta',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
