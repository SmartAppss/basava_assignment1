# Generated by Django 4.2.5 on 2023-09-14 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainee_app', '0002_alter_userinput_doj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinput',
            name='TrainingDuration',
            field=models.CharField(max_length=50),
        ),
    ]
