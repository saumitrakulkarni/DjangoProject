# Generated by Django 5.1.4 on 2024-12-12 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loginify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]