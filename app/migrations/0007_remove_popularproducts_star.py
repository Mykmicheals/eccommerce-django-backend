# Generated by Django 3.2.8 on 2022-02-18 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_popularproducts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popularproducts',
            name='star',
        ),
    ]