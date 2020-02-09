# Generated by Django 3.0.3 on 2020-02-09 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messes',
            fields=[
                ('messID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('messName', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('rollNo', models.IntegerField()),
                ('pref', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('messID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messiah_api.Messes')),
            ],
        ),
        migrations.CreateModel(
            name='Visited',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=25)),
                ('mealType', models.CharField(max_length=15)),
                ('messID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messiah_api.Messes')),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messiah_api.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=100)),
                ('messID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messiah_api.Messes')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menuID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('day', models.CharField(max_length=10)),
                ('nameOfFood', models.CharField(max_length=15)),
                ('mealType', models.CharField(max_length=15)),
                ('messID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messiah_api.Messes')),
            ],
        ),
        migrations.CreateModel(
            name='foodStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preparedQ', models.IntegerField()),
                ('consumedQ', models.IntegerField()),
                ('leftoverQ', models.IntegerField()),
                ('date', models.CharField(max_length=25)),
                ('menuID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messiah_api.Menu')),
            ],
        ),
    ]
