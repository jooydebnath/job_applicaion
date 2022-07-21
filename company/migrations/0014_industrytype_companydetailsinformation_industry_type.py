# Generated by Django 4.0.6 on 2022-07-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_remove_companydetailsinformation_industry_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndustryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='companydetailsinformation',
            name='industry_type',
            field=models.ManyToManyField(to='company.industrytype'),
        ),
    ]