# Generated by Django 3.0.7 on 2021-02-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_auto_20210216_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='urlname',
            field=models.SlugField(default='slug', max_length=100, unique=True, verbose_name='URLNAME'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
