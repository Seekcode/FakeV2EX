# Generated by Django 2.0.2 on 2018-03-09 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0026_topic_comment_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='comment_num',
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.TextField(blank=True, max_length=20000, null=True, verbose_name='Topic 评论'),
        ),
    ]
