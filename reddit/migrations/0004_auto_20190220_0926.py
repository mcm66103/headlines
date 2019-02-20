# Generated by Django 2.1.7 on 2019-02-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0003_auto_20190220_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='redditpost',
            name='selftext',
            field=models.TextField(default='/msp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='redditpost',
            name='subreddit_prefix',
            field=models.CharField(default='/msp', max_length=255),
            preserve_default=False,
        ),
    ]