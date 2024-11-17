# Generated by Django 4.2.16 on 2024-11-14 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_site_app', '0002_remove_project_pics_alter_menu_background_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='dj_site_app/backgrounds/'),
        ),
        migrations.DeleteModel(
            name='ProjectImage',
        ),
    ]