# Generated by Django 3.0.6 on 2020-06-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Card_Game_App', '0004_auto_20200606_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]