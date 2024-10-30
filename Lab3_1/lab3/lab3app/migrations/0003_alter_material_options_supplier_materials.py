# Generated by Django 5.1.2 on 2024-10-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3app', '0002_alter_material_options_alter_supplier_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'managed': False},
        ),
        migrations.AddField(
            model_name='supplier',
            name='materials',
            field=models.ManyToManyField(related_name='materials', to='lab3app.material'),
        ),
    ]