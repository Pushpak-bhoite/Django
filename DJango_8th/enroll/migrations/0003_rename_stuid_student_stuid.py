# Generated by Django 4.1.2 on 2022-11-06 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_rename_stuemail_student_stuemail_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stuid',
            new_name='stuID',
        ),
    ]
