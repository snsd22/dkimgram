# Generated by Django 2.0.3 on 2018-05-21 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20180521_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='images.Image'),
        ),
        migrations.AlterField(
            model_name='like',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='likes', to='images.Image'),
        ),
    ]
