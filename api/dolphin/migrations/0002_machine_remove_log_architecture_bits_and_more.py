# Generated by Django 4.0.6 on 2022-07-13 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dolphin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('machine_id', models.UUIDField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('architecture_bits', models.CharField(max_length=64)),
                ('architecture_linkage', models.CharField(max_length=64)),
                ('machine', models.CharField(max_length=128)),
                ('platform', models.CharField(max_length=128)),
                ('node', models.CharField(max_length=256)),
                ('processor', models.CharField(max_length=256)),
                ('system', models.CharField(max_length=256)),
                ('system_version', models.CharField(max_length=256)),
                ('system_release', models.CharField(max_length=256)),
                ('win32_edition', models.CharField(max_length=256)),
                ('win32_is_iot', models.BooleanField()),
                ('win32_ver_release', models.CharField(max_length=256)),
                ('win32_ver_version', models.CharField(max_length=256)),
                ('win32_ver_csd', models.CharField(max_length=256)),
                ('win32_ver_ptype', models.CharField(max_length=256)),
                ('release', models.CharField(max_length=256)),
                ('versioninfo', models.JSONField()),
                ('libc_lib', models.CharField(max_length=256)),
                ('libc_version', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='log',
            name='architecture_bits',
        ),
        migrations.RemoveField(
            model_name='log',
            name='architecture_linkage',
        ),
        migrations.RemoveField(
            model_name='log',
            name='libc_lib',
        ),
        migrations.RemoveField(
            model_name='log',
            name='libc_version',
        ),
        migrations.RemoveField(
            model_name='log',
            name='machine_id',
        ),
        migrations.RemoveField(
            model_name='log',
            name='node',
        ),
        migrations.RemoveField(
            model_name='log',
            name='platform',
        ),
        migrations.RemoveField(
            model_name='log',
            name='processor',
        ),
        migrations.RemoveField(
            model_name='log',
            name='release',
        ),
        migrations.RemoveField(
            model_name='log',
            name='system',
        ),
        migrations.RemoveField(
            model_name='log',
            name='system_release',
        ),
        migrations.RemoveField(
            model_name='log',
            name='system_version',
        ),
        migrations.RemoveField(
            model_name='log',
            name='versioninfo',
        ),
        migrations.RemoveField(
            model_name='log',
            name='win32_edition',
        ),
        migrations.RemoveField(
            model_name='log',
            name='win32_is_iot',
        ),
        migrations.RemoveField(
            model_name='log',
            name='win32_ver_csd',
        ),
        migrations.RemoveField(
            model_name='log',
            name='win32_ver_ptype',
        ),
        migrations.RemoveField(
            model_name='log',
            name='win32_ver_release',
        ),
        migrations.RemoveField(
            model_name='log',
            name='win32_ver_version',
        ),
        migrations.AlterField(
            model_name='log',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='dolphin.machine'),
        ),
    ]
