# Generated by Django 3.2.5 on 2021-07-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_auto_20210715_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='vehicle_type',
            field=models.CharField(max_length=900),
        ),
    ]
