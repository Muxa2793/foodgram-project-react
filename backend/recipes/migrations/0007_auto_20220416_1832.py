# Generated by Django 2.2.19 on 2022-04-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20220416_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.FileField(blank=True, db_index=True, upload_to='media/', verbose_name='Картинка'),
        ),
    ]
