# Generated by Django 4.0.6 on 2022-07-19 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0030_delete_companydetailsinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetailsInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('are_you_new_entrepreneur', models.CharField(max_length=10)),
                ('year_of_establishment', models.CharField(max_length=4)),
                ('company_size', models.CharField(choices=[('1-15', '1-15 Employees'), ('16-30', '16-30 Employees'), ('31-50', '31-50 Employees')], max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('address', models.TextField(max_length=30)),
                ('industry_type', models.CharField(max_length=40)),
                ('business_description', models.TextField(max_length=500)),
                ('trade_license', models.CharField(max_length=30)),
                ('rl_no', models.CharField(max_length=6)),
                ('website', models.URLField()),
                ('contact_person_designation', models.CharField(max_length=200)),
                ('contact_person_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=14, region=None)),
                ('contact_person_email', models.EmailField(max_length=200)),
                ('accept_all', models.BooleanField()),
                ('zipcode', models.CharField(max_length=5)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('industy_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.industrycategory')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]