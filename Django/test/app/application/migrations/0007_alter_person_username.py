# Generated by Django 5.0.6 on 2024-07-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_alter_person_password_alter_person_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(),
        ),
    ]