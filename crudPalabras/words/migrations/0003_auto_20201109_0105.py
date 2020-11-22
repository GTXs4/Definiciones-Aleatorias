# Generated by Django 3.1.3 on 2020-11-09 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_auto_20201109_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, unique=True, verbose_name='Categoria')),
                ('abbreviation', models.CharField(blank=True, max_length=50, null=True, verbose_name='Abreviatura')),
                ('description', models.TextField(verbose_name='Descripcion')),
            ],
        ),
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(max_length=100, unique=True, verbose_name='Palabra'),
        ),
    ]
