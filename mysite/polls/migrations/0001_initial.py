# Generated by Django 5.0.4 on 2024-04-12 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('is_mobile_verified', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_blocked', models.BooleanField(default=False)),
                ('block_expiration', models.DateTimeField(blank=True, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('unsuccessful_attempts', models.IntegerField(default=0)),
            ],
        ),
    ]
