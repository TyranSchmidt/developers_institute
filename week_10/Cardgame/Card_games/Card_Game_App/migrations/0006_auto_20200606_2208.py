# Generated by Django 3.0.6 on 2020-06-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Card_Game_App', '0005_auto_20200606_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='pokexp',
            field=models.CharField(max_length=50),
        ),
    ]