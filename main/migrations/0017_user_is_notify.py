# Generated by Django 3.2.3 on 2021-06-29 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0016_user_position"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_notify",
            field=models.BooleanField(default=True, verbose_name="Уведомлять?"),
        ),
    ]