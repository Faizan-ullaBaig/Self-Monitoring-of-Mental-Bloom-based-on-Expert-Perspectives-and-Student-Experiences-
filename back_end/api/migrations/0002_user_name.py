# Generated by Django 4.2 on 2023-04-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'), # user name can exist only is email id and password is present so there is dependency
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='Null', max_length=30),
            preserve_default=False,
        ),
    ]
