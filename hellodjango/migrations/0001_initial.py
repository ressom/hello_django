# Generated by Django 3.2.16 on 2023-01-08 22:21

from django.db import migrations, models
import hellodjango.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShareRequest',
            fields=[
                ('GUID', models.UUIDField(primary_key=True, serialize=False)),
                ('requesting_user', models.BigIntegerField()),
                ('share_target_user', models.BigIntegerField()),
                ('created_at', hellodjango.fields.EpochField(created_at=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by_user', models.BigIntegerField()),
                ('for_user', models.BigIntegerField()),
                ('original_url', models.URLField(max_length=5000)),
                ('created_at', hellodjango.fields.EpochField(created_at=True)),
                ('viewed', models.BooleanField(default=False)),
            ],
        ),
    ]
