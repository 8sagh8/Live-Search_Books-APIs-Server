# Generated by Django 3.1.4 on 2021-02-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haq', '0009_auto_20200925_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorized_Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_name', models.CharField(max_length=10)),
            ],
        ),
    ]
