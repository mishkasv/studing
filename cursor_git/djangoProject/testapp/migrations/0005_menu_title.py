# Generated by Django 3.2.5 on 2021-07-31 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_auto_20210731_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='title',
            field=models.CharField(default='default', max_length=50),
        ),
    ]