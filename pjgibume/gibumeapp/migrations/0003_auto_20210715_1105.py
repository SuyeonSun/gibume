# Generated by Django 3.2 on 2021-07-15 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gibumeapp', '0002_auto_20210715_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfume',
            name='product_tag_1',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='perfume',
            name='product_tag_2',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='perfume',
            name='product_tag_3',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='perfume',
            name='product_tag_4',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='perfume',
            name='product_tag_5',
            field=models.CharField(default='', max_length=20),
        ),
    ]
