# Generated by Django 5.0.7 on 2024-07-14 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen1',
            field=models.ImageField(default='default_image.png', upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen2',
            field=models.ImageField(default='default_image.png', upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]