# Generated by Django 5.0.4 on 2024-05-16 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinotruk', '0016_messagedocument'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagedocument',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
