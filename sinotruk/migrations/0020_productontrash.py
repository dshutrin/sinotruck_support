# Generated by Django 5.0.6 on 2024-06-07 13:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinotruk', '0019_alter_product_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOnTrash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_trash', to='sinotruk.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_trash', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]