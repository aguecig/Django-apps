# Generated by Django 2.2.3 on 2019-08-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_auto_20190816_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='function',
            name='point',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
