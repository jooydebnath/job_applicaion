# Generated by Django 4.0.6 on 2022-07-16 13:56

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Skil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skil', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=13, region=None)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.gender')),
                ('skil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.skil')),
            ],
        ),
    ]