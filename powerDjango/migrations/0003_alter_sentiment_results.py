# Generated by Django 3.2.5 on 2021-07-31 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerDjango', '0002_alter_sentiment_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentiment',
            name='results',
            field=models.PositiveBigIntegerField(),
        ),
    ]
