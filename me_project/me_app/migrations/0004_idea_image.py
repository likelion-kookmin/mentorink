# Generated by Django 3.2.4 on 2021-06-25 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me_app', '0003_rename_post_comment_idea'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='idea/'),
        ),
    ]