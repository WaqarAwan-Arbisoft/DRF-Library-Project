# Generated by Django 4.0.6 on 2022-08-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_noofpages'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.FileField(default='', upload_to='images'),
        ),
    ]