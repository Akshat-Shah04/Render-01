# Generated by Django 5.1 on 2025-02-24 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_alter_url_short_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_id',
            field=models.CharField(default='89b61d', max_length=10, unique=True),
        ),
    ]
