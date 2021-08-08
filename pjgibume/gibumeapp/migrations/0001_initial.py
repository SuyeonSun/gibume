# Generated by Django 3.2.5 on 2021-08-04 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30, null=True)),
                ('gender', models.CharField(max_length=30, null=True)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('brand', models.CharField(default='', max_length=200)),
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('perfume_img', models.CharField(default='', max_length=100)),
                ('color', models.CharField(choices=[('red', 'red'), ('ora', 'orange'), ('yel', 'yellow'), ('gre', 'green'), ('blu', 'blue'), ('pur', 'purple'), ('pin', 'pink'), ('whi', 'white'), ('bla', 'black')], max_length=3)),
                ('time', models.CharField(choices=[('per', '퍼퓸'), ('edp', '오드퍼퓸'), ('edt', '오드뜨왈렛'), ('edc', '오드콜로뉴')], max_length=3)),
                ('note_group', multiselectfield.db.fields.MultiSelectField(choices=[('CI', 'Citrus fruits'), ('AR', 'Aromatics'), ('FL', 'Floral'), ('GR', 'Green'), ('FR', 'Fruity'), ('SP', 'Spices'), ('WO', 'Wooded'), ('BA', 'Balsamic')], max_length=23)),
                ('top_note', models.CharField(default='', max_length=400)),
                ('middle_note', models.CharField(default='', max_length=400)),
                ('base_note', models.CharField(default='', max_length=400)),
                ('dislike_users', models.ManyToManyField(blank=True, default='', related_name='dislike_posts', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(blank=True, default='', related_name='like_posts', to=settings.AUTH_USER_MODEL)),
                ('ok_users', models.ManyToManyField(blank=True, default='', related_name='ok_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(default='', max_length=30)),
                ('title', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(default='')),
                ('body', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='gibumeapp/')),
                ('save_users', models.ManyToManyField(blank=True, default='', related_name='save_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default='')),
                ('content', models.TextField(default='')),
                ('author', models.CharField(default='', max_length=30)),
                ('yes_count', models.PositiveIntegerField(default=0)),
                ('no_count', models.PositiveIntegerField(default=0)),
                ('name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gibumeapp.perfume')),
                ('no_users', models.ManyToManyField(blank=True, default='', related_name='no_posts', to=settings.AUTH_USER_MODEL)),
                ('yes_users', models.ManyToManyField(blank=True, default='', related_name='yes_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
