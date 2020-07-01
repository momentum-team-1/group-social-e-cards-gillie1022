# Generated by Django 3.0.7 on 2020-07-01 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0009_auto_20200701_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('Living Coral', 'Living Coral'), ('Ultra Violet', 'Ultra Violet'), ('Greenery', 'Greenery'), ('Rose Quartz', 'Rose Quartz'), ('Serenity', 'Serenity'), ('Marsala', 'Marsala'), ('Radiand Orchid', 'Radiand Orchid'), ('Emerald', 'Emerald'), ('Tangerine Tango', 'Tangerine Tango'), ('Honeysucle', 'Honeysucle'), ('Turquoise', 'Turquoise'), ('Mimosa', 'Mimosa'), ('Blue Izis', 'Blue Izis'), ('Chili Pepper', 'Chili Pepper'), ('Sand Dollar', 'Sand Dollar'), ('Blue Turquoise', 'Blue Turquoise'), ('Tigerlily', 'Tigerlily'), ('Aqua Sky', 'Aqua Sky'), ('True Red', 'True Red'), ('Fuchsia Rose', 'Fuchsia Rose'), ('Cerulean Blue', 'Cerulean Blue')], default='Cerulean Blue', max_length=15),
        ),
        migrations.AlterField(
            model_name='card',
            name='font',
            field=models.CharField(choices=[('Montserrat + Lora (Modern)', 'Montserrat + Lora (Modern)'), ('Prata + Lato (Elegant)', 'Prata + Lato (Elegant)'), ('Archivo Black + Judson (Emphasis)', 'Archivo Black + Judson (Emphasis)')], default='Montserrat + Lora (Modern)', max_length=33),
        ),
    ]