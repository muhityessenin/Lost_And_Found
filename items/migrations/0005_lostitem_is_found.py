# Generated by Django 5.1.6 on 2025-03-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_founditem_user_alter_lostitem_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostitem',
            name='is_found',
            field=models.BooleanField(default=False),
        ),
    ]
