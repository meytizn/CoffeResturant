# Generated by Django 4.0.6 on 2024-08-15 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinematicket', '0005_remove_tag_slug_tag_slug_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food', to='cinematicket.category', verbose_name='دسته بندی محصول  '),
        ),
    ]
