# Generated by Django 3.0.5 on 2021-05-27 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacrawling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=200)),
                ('tags', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='biography',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='brand',
            name='post',
            field=models.ManyToManyField(to='datacrawling.Post'),
        ),
    ]
