# Generated by Django 3.2.7 on 2021-09-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Image',
            field=models.ImageField(default='images/user.png', null=True, upload_to='users %d/%m/%y'),
        ),
    ]
