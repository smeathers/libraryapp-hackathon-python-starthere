# Generated by Django 2.1.5 on 2019-01-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20190114_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]