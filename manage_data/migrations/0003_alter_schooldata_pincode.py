# Generated by Django 4.1.7 on 2023-03-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_data', '0002_rename_school_user_schooldata_school_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooldata',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
    ]
