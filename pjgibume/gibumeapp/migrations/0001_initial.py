from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('brand', models.CharField(default='', max_length=200)),
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('perfume_img', models.CharField(default='', max_length=100)),
                ('color', models.CharField(choices=[('red', 'red'), ('ora', 'orange'), ('yel', 'yellow'), ('gre', 'green'), ('blu', 'blue'), ('pur', 'purple'), ('pin', 'pink'), ('whi', 'white'), ('bla', 'black')], max_length=3)),
                ('time', models.CharField(choices=[('per', '퍼퓸'), ('edp', '오드퍼퓸'), ('edt', '오드뜨왈렛'), ('edc', '오드콜로뉴')], max_length=3)),
                ('love_count', models.PositiveIntegerField(default=0)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('ok_count', models.PositiveIntegerField(default=0)),
                ('dislike_count', models.PositiveIntegerField(default=0)),
                ('hate_count', models.PositiveIntegerField(default=0)),
                ('note_group', multiselectfield.db.fields.MultiSelectField(choices=[('CI', 'Citrus fruits'), ('AR', 'Aromatics'), ('FL', 'Floral'), ('GR', 'Green'), ('FR', 'Fruity'), ('SP', 'Spices'), ('WO', 'Wooded'), ('BA', 'Balsamic')], max_length=23)),
                ('top_note', models.CharField(default='', max_length=400)),
                ('middle_note', models.CharField(default='', max_length=400)),
                ('base_note', models.CharField(default='', max_length=400)),
            ],
        ),
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
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default='')),
                ('content', models.TextField(default='')),
                ('name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gibumeapp.perfume')),
            ],
        ),
    ]
