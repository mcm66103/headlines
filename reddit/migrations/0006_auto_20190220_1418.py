# Generated by Django 2.1.7 on 2019-02-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0005_auto_20190220_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='associated_post',
            field=models.ManyToManyField(related_name='associated_post', to='reddit.RedditPost'),
        ),
    ]
