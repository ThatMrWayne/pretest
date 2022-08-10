# Generated by Django 3.0.9 on 2022-08-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_number', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('total_price', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]