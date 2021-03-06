# Generated by Django 2.0.2 on 2018-03-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0021_nodelink'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nodelink',
            options={'verbose_name': 'Link', 'verbose_name_plural': 'Link'},
        ),
        migrations.RemoveField(
            model_name='nodelink',
            name='click_num',
        ),
        migrations.RemoveField(
            model_name='nodelink',
            name='content',
        ),
        migrations.RemoveField(
            model_name='nodelink',
            name='html_content',
        ),
        migrations.RemoveField(
            model_name='nodelink',
            name='topic_sn',
        ),
        migrations.AddField(
            model_name='nodelink',
            name='desc',
            field=models.CharField(default='', max_length=120, verbose_name='Link 简介'),
        ),
        migrations.AddField(
            model_name='nodelink',
            name='link',
            field=models.CharField(default='', max_length=50, unique=True, verbose_name='连接地址'),
        ),
        migrations.AlterField(
            model_name='nodelink',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='Link 标题'),
        ),
    ]
