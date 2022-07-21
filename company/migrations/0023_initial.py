# Generated by Django 4.0.6 on 2022-07-17 11:02

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0022_remove_companydetailsinformation_industry_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_requirements', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EducationalRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educaton', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentStatu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='IndustryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndustryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='WorkPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_place', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='JobRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy', models.IntegerField()),
                ('job_context', models.TextField(max_length=400)),
                ('job_responsibilities', models.TextField(max_length=10000)),
                ('location', models.CharField(max_length=20)),
                ('benefits', models.TextField(max_length=300)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('additional_requirements', models.ManyToManyField(to='company.additionalrequirement')),
                ('educational_requirement', models.ManyToManyField(to='company.educationalrequirement')),
                ('employment_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.employmentstatu')),
                ('salary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.salary')),
                ('work_experience', models.ManyToManyField(to='company.experience')),
                ('work_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.workplace')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyDetailsInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('are_you_new_entrepreneur', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=20)),
                ('year_of_establishment', models.CharField(max_length=4)),
                ('company_size', models.CharField(choices=[('1-15', '1-15 Employees'), ('16-30', '16-30 Employees'), ('31-50', '31-50 Employees')], max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('address', models.TextField(max_length=30)),
                ('business_description', models.TextField(max_length=500)),
                ('trade_license', models.CharField(max_length=30)),
                ('rl_no', models.CharField(max_length=6)),
                ('website', models.URLField()),
                ('contact_person_name', models.CharField(max_length=200)),
                ('contact_person_designation', models.CharField(max_length=200)),
                ('contact_person_email', models.EmailField(max_length=200)),
                ('contact_person_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=13, region=None)),
                ('active_user', models.BooleanField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('industry_type', models.ManyToManyField(to='company.industrytype')),
                ('industy_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.industrycategory')),
            ],
        ),
    ]