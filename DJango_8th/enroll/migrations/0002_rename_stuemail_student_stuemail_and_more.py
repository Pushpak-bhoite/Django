# Generated by Django 4.1.2 on 2022-11-06 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stuEmail',
            new_name='stuemail',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stuID',
            new_name='stuid',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stuName',
            new_name='stuname',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stuPass',
            new_name='stupass',
        ),
    ]
