# Generated by Django 3.2.4 on 2021-06-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_alter_character_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('surname', models.CharField(blank=True, max_length=30)),
                ('books', models.ManyToManyField(to='demo.Book')),
            ],
        ),
    ]