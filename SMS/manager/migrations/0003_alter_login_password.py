# Generated by Django 5.0.3 on 2024-04-08 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_login_user_type_alter_login_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='Password',
            field=models.CharField(max_length=25),
        ),
    ]
