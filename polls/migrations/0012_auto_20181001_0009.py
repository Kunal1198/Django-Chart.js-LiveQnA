# Generated by Django 2.0.3 on 2018-09-30 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20180930_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page1',
            old_name='Total_no_of_people_using',
            new_name='card',
        ),
        migrations.RenameField(
            model_name='page1',
            old_name='How_was_the_event',
            new_name='question',
        ),
    ]
