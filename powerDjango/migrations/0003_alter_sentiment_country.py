# Generated by Django 3.2.5 on 2021-08-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerDjango', '0002_alter_sentiment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentiment',
            name='country',
            field=models.CharField(choices=[('United States of America', 'United States of America'), ('Canada', 'Canada'), ('Mexico', 'Mexico'), ('Europe', 'Europe'), ('Japan', 'Japan'), ('South Korea', 'South Korea')], max_length=24),
        ),
    ]
