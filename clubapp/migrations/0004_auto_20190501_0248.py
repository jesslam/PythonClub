# Generated by Django 2.2 on 2019-05-01 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubapp', '0003_auto_20190430_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetingminutes',
            old_name='meetingid',
            new_name='meetingtitle',
        ),
    ]
