# Generated by Django 2.0.3 on 2018-09-28 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20180927_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page1',
            name='relevance',
        ),
        migrations.RemoveField(
            model_name='page1',
            name='status',
        ),
    ]