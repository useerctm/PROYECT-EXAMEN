
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imagen1',
            field=models.ImageField(default='default_image.jpg', upload_to='product_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='imagen2',
            field=models.ImageField(default='default_image.jpg', upload_to='product_images'),
        ),
    ]
