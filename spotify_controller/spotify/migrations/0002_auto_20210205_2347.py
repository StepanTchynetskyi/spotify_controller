# Generated by Django 3.1 on 2021-02-05 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='refresh_token',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
