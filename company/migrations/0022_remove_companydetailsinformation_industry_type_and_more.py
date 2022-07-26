# Generated by Django 4.0.6 on 2022-07-17 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0021_additionalrequirement_educationalrequirement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companydetailsinformation',
            name='industry_type',
        ),
        migrations.RemoveField(
            model_name='companydetailsinformation',
            name='industy_category',
        ),
        migrations.RemoveField(
            model_name='jobrequest',
            name='additional_requirements',
        ),
        migrations.RemoveField(
            model_name='jobrequest',
            name='educational_requirement',
        ),
        migrations.RemoveField(
            model_name='jobrequest',
            name='employment_status',
        ),
        migrations.RemoveField(
            model_name='jobrequest',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='jobrequest',
            name='work_experience',
        ),
        migrations.RemoveField(
            model_name='jobrequest',
            name='work_place',
        ),
        migrations.DeleteModel(
            name='AdditionalRequirement',
        ),
        migrations.DeleteModel(
            name='CompanyDetailsInformation',
        ),
        migrations.DeleteModel(
            name='EducationalRequirement',
        ),
        migrations.DeleteModel(
            name='EmploymentStatu',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='IndustryCategory',
        ),
        migrations.DeleteModel(
            name='IndustryType',
        ),
        migrations.DeleteModel(
            name='JobRequest',
        ),
        migrations.DeleteModel(
            name='Salary',
        ),
        migrations.DeleteModel(
            name='WorkPlace',
        ),
    ]
