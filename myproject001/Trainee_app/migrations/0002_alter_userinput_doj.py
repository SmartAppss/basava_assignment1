# Generated by Django 4.2.5 on 2023-09-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainee_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinput',
            name='DOJ',
            field=models.DateField(),
        ),
    ]
