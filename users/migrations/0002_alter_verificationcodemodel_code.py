# Generated by Django 5.0.6 on 2024-06-08 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationcodemodel',
            name='code',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
