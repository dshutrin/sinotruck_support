# Generated by Django 4.2.9 on 2024-05-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinotruk', '0018_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mark',
            field=models.CharField(max_length=255, null=True, verbose_name='Марка'),
        ),
    ]