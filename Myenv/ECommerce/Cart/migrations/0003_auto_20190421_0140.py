# Generated by Django 2.2 on 2019-04-20 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0002_item_imglink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='imglink',
            field=models.ImageField(upload_to='Gallery'),
        ),
    ]
