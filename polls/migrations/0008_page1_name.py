# Generated by Django 2.0.3 on 2018-09-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20180929_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='page1',
            name='name',
            field=models.CharField(choices=[('AMS', 'Amsterdam'), ('ROT', 'Rotterdam'), ('THE', 'The Hague'), ('UTR', 'Utrecht')], default='AMS', max_length=3),
        ),
    ]
