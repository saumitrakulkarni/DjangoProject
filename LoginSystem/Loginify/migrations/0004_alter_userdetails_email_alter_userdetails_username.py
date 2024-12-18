# Generated by Django 5.1.4 on 2024-12-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loginify', '0003_alter_userdetails_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='email',
            field=models.EmailField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
