# Generated by Django 4.0.6 on 2022-07-22 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidates', '0010_remove_generalcategory_skils_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialSkilledCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=13, region=None)),
                ('agree', models.BooleanField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('skils', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.skils')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Salary', models.CharField(max_length=8)),
                ('resume', models.FileField(upload_to='documents/')),
                ('accept_all', models.BooleanField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=13, region=None)),
                ('agree', models.BooleanField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('skils', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.skils')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AutismCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=13, region=None)),
                ('autism_id', models.CharField(max_length=20)),
                ('agree', models.BooleanField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('skils', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.skils')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
