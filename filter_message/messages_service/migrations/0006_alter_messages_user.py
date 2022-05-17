# Generated by Django 4.0.4 on 2022-05-17 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messages_service', '0005_alter_messages_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_is', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
