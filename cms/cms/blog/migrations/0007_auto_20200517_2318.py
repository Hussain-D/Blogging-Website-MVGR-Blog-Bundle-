# Generated by Django 2.2.10 on 2020-05-17 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200514_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
