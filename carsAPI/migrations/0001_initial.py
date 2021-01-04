# Generated by Django 3.1.5 on 2021-01-04 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make_name', models.CharField(max_length=255, verbose_name='Car Make Name')),
                ('model_name', models.CharField(max_length=255, verbose_name='Car Model Name')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='CarRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Neutral'), (4, 'Good'), (5, 'Very Good')], default=3, verbose_name='Rating')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Car', to='carsAPI.cars')),
            ],
            options={
                'verbose_name': 'Car rate',
                'verbose_name_plural': 'Cars ratings',
            },
        ),
    ]
