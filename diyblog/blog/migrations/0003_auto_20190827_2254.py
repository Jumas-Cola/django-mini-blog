# Generated by Django 2.1.11 on 2019-08-27 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190827_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='description',
        ),
    ]
