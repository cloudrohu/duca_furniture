# Generated by Django 5.0.1 on 2024-10-29 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_additional_information_alter_brand_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='arm_style',
        ),
        migrations.RemoveField(
            model_name='product',
            name='assembly',
        ),
        migrations.RemoveField(
            model_name='product',
            name='back_style',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='product',
            name='embellishment_feature',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fill_material',
        ),
        migrations.RemoveField(
            model_name='product',
            name='height',
        ),
        migrations.RemoveField(
            model_name='product',
            name='height_base_to_top',
        ),
        migrations.RemoveField(
            model_name='product',
            name='included_components',
        ),
        migrations.RemoveField(
            model_name='product',
            name='item_depth_front_to_back',
        ),
        migrations.RemoveField(
            model_name='product',
            name='item_shape',
        ),
        migrations.RemoveField(
            model_name='product',
            name='item_width_side_to_side',
        ),
        migrations.RemoveField(
            model_name='product',
            name='material',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pattern',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quality_certification',
        ),
        migrations.RemoveField(
            model_name='product',
            name='room_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='seat_back_interior_height',
        ),
        migrations.RemoveField(
            model_name='product',
            name='seat_depth',
        ),
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='upholstery_color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='width',
        ),
        migrations.RemoveField(
            model_name='product',
            name='additional_information',
        ),
        migrations.AddField(
            model_name='additional_information',
            name='additional_type',
            field=models.CharField(choices=[('Quality_Certification', 'Quality_Certification'), ('Embellishment_Feature', 'Embellishment_Feature'), ('Back_Style', 'Back_Style'), ('Depth', 'Depth'), ('Material', 'Material'), ('Width', 'Width'), ('Height', 'Height'), ('Arm_Style', 'Arm_Style'), ('Seat_Back_Interior_Height', 'Seat_Back_Interior_Height'), ('Assembly', 'Assembly'), ('Item_Shape', 'Item_Shape'), ('Seat_Depth', 'Seat_Depth'), ('Type', 'Type'), ('Room_Type', 'Room_Type'), ('Size', 'Size'), ('Others', 'Others')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='additional_information',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Arm_Style',
        ),
        migrations.DeleteModel(
            name='Assembly',
        ),
        migrations.DeleteModel(
            name='Back_Style',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Depth',
        ),
        migrations.DeleteModel(
            name='Embellishment_Feature',
        ),
        migrations.DeleteModel(
            name='Fill_Material',
        ),
        migrations.DeleteModel(
            name='Height',
        ),
        migrations.DeleteModel(
            name='Height_Base_to_Top',
        ),
        migrations.DeleteModel(
            name='Included_Components',
        ),
        migrations.DeleteModel(
            name='Item_Depth_Front_to_Back',
        ),
        migrations.DeleteModel(
            name='Item_Shape',
        ),
        migrations.DeleteModel(
            name='Item_Width_Side_to_Side',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='Pattern',
        ),
        migrations.DeleteModel(
            name='Quality_Certification',
        ),
        migrations.DeleteModel(
            name='Room_Type',
        ),
        migrations.DeleteModel(
            name='Seat_Back_Interior_Height',
        ),
        migrations.DeleteModel(
            name='Seat_Depth',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.DeleteModel(
            name='Upholstery_Color',
        ),
        migrations.DeleteModel(
            name='Width',
        ),
    ]
