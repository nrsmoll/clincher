# Generated by Django 2.2 on 2019-06-20 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalviewer', '0002_auto_20190521_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='user',
            new_name='patid',
        ),
    ]