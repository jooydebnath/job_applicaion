# Generated by Django 4.0.6 on 2022-07-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companydetailsinformation',
            name='industry_type',
        ),
        migrations.AddField(
            model_name='companydetailsinformation',
            name='industry_type',
            field=models.ManyToManyField(to='company.industrytype'),
        ),
    ]
