# Generated by Django 4.0.4 on 2022-06-26 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_reviewrating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]
