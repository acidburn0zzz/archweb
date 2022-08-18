# Generated by Django 4.1 on 2022-08-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devel', '0008_alter_userprofile_repos_auth_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='public_email',
            field=models.EmailField(help_text='Required field', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website_rss',
            field=models.URLField(blank=True, help_text='RSS Feed of your website for planet.archlinux.org', null=True),
        ),
    ]
