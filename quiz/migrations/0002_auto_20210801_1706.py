# Generated by Django 3.2.5 on 2021-08-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer2',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='answer3',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='answer4',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]