# Generated by Django 2.0.3 on 2018-09-30 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20180930_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page1',
            name='How_was_the_event',
            field=models.CharField(choices=[('E', 'Excellent'), ('G', 'Good'), ('A', 'Average'), ('P', 'Poor')], default='G', max_length=10),
        ),
    ]