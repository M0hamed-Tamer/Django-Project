# Generated by Django 5.0.7 on 2024-08-06 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='work',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Job.category'),
        ),
    ]
