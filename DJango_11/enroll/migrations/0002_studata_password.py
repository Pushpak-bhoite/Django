# Generated by Django 4.1.2 on 2022-11-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studata',
            name='password',
            field=models.CharField(default='Empty', max_length=35),
        ),
    ]