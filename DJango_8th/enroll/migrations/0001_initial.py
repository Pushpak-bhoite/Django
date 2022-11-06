# Generated by Django 4.1.2 on 2022-11-06 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuID', models.IntegerField()),
                ('stuName', models.CharField(max_length=70)),
                ('stuEmail', models.EmailField(max_length=70)),
                ('stuPass', models.CharField(max_length=70)),
            ],
        ),
    ]
