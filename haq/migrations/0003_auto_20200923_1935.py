# Generated by Django 3.1.1 on 2020-09-23 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haq', '0002_book_category_language_need_person_religion_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='_p_name',
            field=models.CharField(max_length=40),
        ),
    ]
