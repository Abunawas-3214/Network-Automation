# Generated by Django 4.2.9 on 2024-01-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=255)),
                ('hostname', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('ssh_port', models.IntegerField(default=22)),
                ('vendor', models.CharField(choices=[('mikrotik', 'Mikrotik'), ('cisco', 'Cisco')], max_length=255)),
            ],
        ),
    ]
