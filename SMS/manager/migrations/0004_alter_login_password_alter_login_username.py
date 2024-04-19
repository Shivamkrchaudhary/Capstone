# Generated by Django 5.0.3 on 2024-04-08 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_alter_login_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='Password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='login',
            name='Username',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
