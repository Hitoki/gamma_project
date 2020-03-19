# Generated by Django 3.0.2 on 2020-03-15 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ALL', 'All'), ('CLS', 'Classic'), ('CAD', 'Crime and Detective'), ('DRA', 'Drama'), ('RMC', 'Romance'), ('HRR', 'Horror'), ('WRC', 'Warcraft')], default='ALL', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('book_author', models.CharField(max_length=75)),
                ('image', models.ImageField(default='default.jpg', upload_to='products_pics')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Category')),
            ],
        ),
    ]
