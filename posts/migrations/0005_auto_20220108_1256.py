# Generated by Django 3.2.9 on 2022-01-08 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_writer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['today_date']},
        ),
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(null=True, upload_to='posts/'),
        ),
    ]
