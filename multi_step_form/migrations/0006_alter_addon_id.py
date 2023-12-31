# Generated by Django 4.2.2 on 2023-07-03 09:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('multi_step_form', '0005_alter_addon_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addon',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
