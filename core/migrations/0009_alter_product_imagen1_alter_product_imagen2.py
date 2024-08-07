
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_product_imagen1_alter_product_imagen2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagen1',
            field=models.ImageField(default='default_image.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen2',
            field=models.ImageField(default='default_image.png', upload_to=''),
        ),
    ]
