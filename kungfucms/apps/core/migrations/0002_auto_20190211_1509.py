# Generated by Django 2.1.3 on 2019-02-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logrecord',
            name='asctime',
            field=models.DateTimeField(verbose_name='时间'),
        ),
    ]