# Generated by Django 4.1 on 2022-09-01 11:23

from django.db import migrations, models
import petstragram.main_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', validators=[petstragram.main_app.validators.validate_file_max_size_in_mb])),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('tagget_pets', models.ManyToManyField(to='main_app.pet')),
            ],
        ),
    ]
