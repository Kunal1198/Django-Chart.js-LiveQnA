# Generated by Django 2.0.3 on 2018-10-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_page1_question1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page1',
            name='question1',
            field=models.CharField(default=True, max_length=50),
        ),
    ]
