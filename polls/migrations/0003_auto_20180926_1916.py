# Generated by Django 2.0.3 on 2018-09-26 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180926_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='user1',
            new_name='username',
        ),
    ]
