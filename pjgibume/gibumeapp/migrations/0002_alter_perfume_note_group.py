# Generated by Django 3.2.4 on 2021-07-17 08:55

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gibumeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfume',
            name='note_group',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('CI', 'Citrus fruits'), ('AR', 'Aromatics'), ('FL', 'Floral'), ('GR', 'Green'), ('FR', 'Fruity'), ('SP', 'Spices'), ('WO', 'Wooded'), ('BA', 'Balsamic')], max_length=2),
        ),
    ]
