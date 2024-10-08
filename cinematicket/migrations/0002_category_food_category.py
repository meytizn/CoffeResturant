# Generated by Django 4.0.6 on 2024-08-12 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinematicket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان دسته بندی ')),
                ('slug', models.SlugField(verbose_name='عنوان دسته بندی لاتین ')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='زمان انتشار')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinematicket.category', verbose_name='دسته بندی محصول  '),
        ),
    ]
