# Generated by Django 4.2.5 on 2023-11-08 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_secret',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
        migrations.AddField(
            model_name='user',
            name='email_verify',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP')], default='USD', max_length=4),
        ),
        migrations.AlterField(
            model_name='user',
            name='languages',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('ru', 'Russian'), ('zh', 'Chinese'), ('KRW', 'Korean')], default='en', max_length=4),
        ),
    ]
