# Generated by Django 2.0.7 on 2018-07-08 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180708_0110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipient',
            old_name='groups',
            new_name='group',
        ),
    ]