# Generated by Django 3.2.5 on 2021-08-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerDjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentiment',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]