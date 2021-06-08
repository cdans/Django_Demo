# Generated by Django 3.2.4 on 2021-06-08 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('description', models.TextField(blank=True, max_length=256)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
