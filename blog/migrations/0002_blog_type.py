# Generated by Django 3.2.9 on 2022-02-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='type',
            field=models.CharField(choices=[('s', 'suche'), ('b', 'biete')], default='s', max_length=1),
        ),
    ]
