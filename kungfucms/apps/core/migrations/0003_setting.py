# Generated by Django 2.1.8 on 2019-06-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190211_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted time')),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('value', models.CharField(blank=True, max_length=255, null=True, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
                'ordering': ['-id'],
            },
        ),
    ]
