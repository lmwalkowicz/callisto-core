# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-30 16:15
from __future__ import unicode_literals

from django.db import migrations


def update_content_types(source, apps, schema_editor):
    db_alias = schema_editor.connection.alias
    ContentType = apps.get_model('contenttypes', 'ContentType')
    content_type = ContentType.objects.using(db_alias).filter(
        app_label=source,
        model='emailnotification',
    ).delete()

def update_content_types_forward(apps, schema_editor):
    update_content_types('delivery', apps, schema_editor)

def update_content_types_reverse(apps, schema_editor):
    update_content_types('notification', apps, schema_editor)

class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0009_to_address_to_textfield'),
    ]

    database_operations = [
        migrations.AlterModelTable('EmailNotification', 'notification_emailnotification')
    ]

    state_operations = [
        migrations.DeleteModel('EmailNotification')
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations,
        ),
        migrations.RunPython(
            update_content_types_forward,
            update_content_types_reverse,
        ),
    ]
