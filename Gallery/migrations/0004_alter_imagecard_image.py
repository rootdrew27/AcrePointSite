# Generated by Django 4.2.3 on 2023-07-24 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0003_imagecard_title_alter_category_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecard',
            name='image',
            field=models.ImageField(height_field='360', upload_to='Gallery/images', width_field='480'),
        ),
    ]
