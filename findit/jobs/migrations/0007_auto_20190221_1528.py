# Generated by Django 2.1.7 on 2019-02-21 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20190221_1503'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Requirements',
            new_name='Requirement',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='decription',
            new_name='description',
        ),
    ]