# Generated by Django 4.1.3 on 2023-11-18 21:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('name', models.TextField(verbose_name='World Name')),
                ('server', models.TextField(verbose_name='Server')),
                ('datacenter', models.TextField(verbose_name='Data Center')),
            ],
            options={
                'verbose_name_plural': 'Worlds',
            },
        ),
    ]
