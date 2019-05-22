# Generated by Django 2.0.4 on 2019-05-21 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='medicare1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='medicare2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]