# Generated by Django 3.2.8 on 2022-03-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_each_id_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='each',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
