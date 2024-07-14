
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_cart_cartitem_cart_products_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
