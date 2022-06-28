# Generated by Django 2.2.7 on 2019-12-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('bookid', models.IntegerField()),
                ('bookname', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='bphoto')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]