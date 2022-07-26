# Generated by Django 4.0.6 on 2022-07-16 15:28

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialSkilledCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=13, region=None)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.gender')),
                ('skil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.skil')),
            ],
        ),
    ]
