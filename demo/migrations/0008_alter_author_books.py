# Generated by Django 3.2.4 on 2021-06-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20210612_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='demo.Book'),
        ),
    ]
