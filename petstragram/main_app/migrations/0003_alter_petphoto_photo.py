# Generated by Django 4.1 on 2022-09-10 16:59

from django.db import migrations, models
import petstragram.main_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_petphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to='photos', validators=[petstragram.main_app.validators.validate_file_max_size_in_mb]),
        ),
    ]
