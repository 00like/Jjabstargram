# Generated by Django 3.2.5 on 2021-08-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(default='photos/no_image.png', upload_to='photos/%Y/%m/%d'),
        ),
    ]
