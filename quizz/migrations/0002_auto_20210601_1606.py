# Generated by Django 3.2.3 on 2021-06-01 15:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tentativa',
            old_name='attempter',
            new_name='pessoa',
        ),
        migrations.RemoveField(
            model_name='resposta',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tentativa',
            name='pergunta',
        ),
        migrations.RemoveField(
            model_name='tentativa',
            name='resposta',
        ),
        migrations.AddField(
            model_name='tentativa',
            name='pontuacao_total',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=200)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('nr_tentativas', models.PositiveIntegerField()),
                ('tempo_limite_mins', models.PositiveIntegerField()),
                ('perguntas', models.ManyToManyField(to='quizz.Pergunta')),
            ],
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='quizz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.quizz'),
        ),
        migrations.AlterField(
            model_name='tentativa',
            name='quizz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.quizz'),
        ),
        migrations.DeleteModel(
            name='Quizzes',
        ),
    ]