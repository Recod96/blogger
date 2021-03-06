# Generated by Django 2.2.7 on 2019-11-30 00:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191129_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostParagraphs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='static/blog/image/')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 30, 0, 43, 37, 245436, tzinfo=utc)),
        ),
    ]
