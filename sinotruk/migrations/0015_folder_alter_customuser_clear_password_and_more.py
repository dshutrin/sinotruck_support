# Generated by Django 5.0.4 on 2024-05-15 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinotruk', '0014_alter_customuser_dealer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Папка')),
            ],
            options={
                'verbose_name': 'Папка',
                'verbose_name_plural': 'Папки',
            },
        ),
        migrations.AlterField(
            model_name='customuser',
            name='clear_password',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Пароль'),
        ),
        migrations.AddField(
            model_name='document',
            name='folder',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='sinotruk.folder', verbose_name='Папка'),
        ),
    ]