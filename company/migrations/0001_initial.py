# Generated by Django 4.0.6 on 2022-07-13 07:30

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetailsInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('are_you_new_entrepreneur', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=20)),
                ('year_of_establishment', models.CharField(max_length=4)),
                ('Country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
    ]
