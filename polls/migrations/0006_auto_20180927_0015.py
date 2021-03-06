# Generated by Django 2.0.3 on 2018-09-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_page1_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page1',
            name='gender',
        ),
        migrations.AddField(
            model_name='page1',
            name='relevance',
            field=models.IntegerField(choices=[(1, 'Unread'), (2, 'Read')], default=1),
        ),
        migrations.AddField(
            model_name='page1',
            name='status',
            field=models.IntegerField(choices=[(1, 'Not relevant'), (2, 'Review'), (3, 'Maybe relevant'), (4, 'Relevant'), (5, 'Leading candidate')], default=1),
        ),
    ]
