# Generated by Django 2.2.1 on 2019-06-10 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='added',
            new_name='updated',
        ),
    ]