# Generated by Django 5.1.7 on 2025-05-13 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_platform', '0018_onlinereview_review_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerreview',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
