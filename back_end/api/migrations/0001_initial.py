# Generated by Django 4.2 on 2023-04-17 18:27

from django.db import migrations, models #importing 2 classes migration and models 
#migration is used to update daata in database without losing existing data
#models high level object oriented interface for interacting with django application


class Migration(migrations.Migration): # used to send data to backend 

    initial = True #since true itll send data to backend if false doesnt send 

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)), #used to create and validate as email field as its primary key
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
