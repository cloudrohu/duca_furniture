# Generated by Django 5.0.1 on 2024-10-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_banner_options_alter_offer_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='header_footer_color',
            new_name='nav_color_2',
        ),
        migrations.AddField(
            model_name='setting',
            name='nav_color_1',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='setting',
            name='nav_color_3',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]