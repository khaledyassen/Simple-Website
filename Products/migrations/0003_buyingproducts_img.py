# Generated by Django 3.2.7 on 2021-09-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_rename_zip_buyingproducts_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyingproducts',
            name='Img',
            field=models.ImageField(blank=True, null=True, upload_to='aniamls %d/%m/%y'),
        ),
    ]
