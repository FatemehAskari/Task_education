# Generated by Django 5.0.6 on 2024-07-14 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_person_password_person_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=5),
        ),
    ]
