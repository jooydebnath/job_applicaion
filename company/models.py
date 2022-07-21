from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class IndustryCategory(models.Model):
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.category

class CompanyDetailsInformation(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    EMPLOYEES_CHOICES = (
        ('1-15', '1-15 Employees'),
        ('16-30', '16-30 Employees'),
        ('31-50', '31-50 Employees'),

    )
    company_name = models.CharField(max_length=100)
    are_you_new_entrepreneur = models.CharField(max_length=10)
    year_of_establishment = models.CharField(max_length=4)
    company_size = models.CharField(choices=EMPLOYEES_CHOICES, max_length=20)
    country = CountryField()
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    address = models.TextField(max_length=30)
    industy_category = models.ForeignKey(IndustryCategory, on_delete=models.CASCADE)
    industry_type = models.CharField(max_length=40)
    business_description = models.TextField(max_length=500)
    trade_license = models.CharField(max_length=30)
    rl_no = models.CharField(max_length=6)
    website = models.URLField(max_length=200)
    contact_person_name = models.CharField(max_length=200)
    contact_person_designation = models.CharField(max_length=200)
    contact_person_phone = PhoneNumberField(max_length=14)
    contact_person_email = models.EmailField(max_length=200)
    accept_all = models.BooleanField()
    zipcode = models.CharField(max_length=5)
    datetime = models.DateTimeField(auto_now_add=True)

class EmploymentStatu(models.Model):
    status = models.CharField(max_length=10)

class EducationalRequirement(models.Model):
    educaton = models.CharField(max_length=300)

class WorkPlace(models.Model):
    word_place = models.CharField(max_length=20)

class Experience(models.Model):
    experience = models.CharField(max_length=150)

class AdditionalRequirement(models.Model):
    additional_requirements = models.CharField(max_length=200)

class Salary(models.Model):
    salary = models.CharField(max_length=150)


class JobRequest(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    vacancy = models.IntegerField()
    job_context = models.TextField(max_length=400)
    job_responsibilities = models.TextField(max_length=10000)
    employment_status = models.ForeignKey(EmploymentStatu, on_delete=models.CASCADE)
    educational_requirement = models.ManyToManyField(EducationalRequirement)
    work_place = models.ForeignKey(WorkPlace, on_delete=models.CASCADE)
    work_experience = models.ManyToManyField(Experience)
    additional_requirements = models.ManyToManyField(AdditionalRequirement)
    location = models.CharField(max_length=20)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    benefits = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now_add=True)




