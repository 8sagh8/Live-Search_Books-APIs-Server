# Generated by Django 3.1.4 on 2021-03-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haq', '0010_authorized_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(max_length=1),
        ),
    ]
