# Generated by Django 3.2.5 on 2021-07-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=30)),
                ('c_plus_plus_level', models.IntegerField(default=0)),
                ('c_level', models.IntegerField(default=0)),
                ('rust_level', models.IntegerField(default=0)),
                ('python_level', models.IntegerField(default=0)),
                ('java_level', models.IntegerField(default=0)),
            ],
        ),
    ]
