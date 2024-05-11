# Generated by Django 5.0.4 on 2024-05-03 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinotruk', '0005_document_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dealer_name',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='document',
            name='owner',
            field=models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Владелец'),
        ),
    ]