# Generated by Django 3.2.4 on 2021-06-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pw', '0006_auto_20210604_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios_Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios_Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_text', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios_Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_text', models.CharField(max_length=15)),
                ('nota_valor', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.AddField(
            model_name='comentarios_avaliacao',
            name='categoria',
            field=models.ManyToManyField(to='pw.Comentarios_Categorias'),
        ),
        migrations.AddField(
            model_name='comentarios_avaliacao',
            name='nota',
            field=models.ManyToManyField(to='pw.Comentarios_Notas'),
        ),
    ]