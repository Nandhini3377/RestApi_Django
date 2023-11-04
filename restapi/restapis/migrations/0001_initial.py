# Generated by Django 4.2.7 on 2023-11-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='productname', max_length=30)),
                ('price', models.CharField(default='Rs.0', max_length=10)),
                ('imgurl', models.URLField()),
            ],
        ),
    ]