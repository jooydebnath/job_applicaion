from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from company.models import *

ENTREPRENEUR_CHOICE = [
    ('Y', 'Yes'),
    ('N', 'No')
]

INDUSTRYTYPE_CHOICE = [
    ('Software Company', 'Software Company'),
    ('Call Center', 'Call Center'),
    ('E-commerce', 'E-commerce'),
    ('Banks', 'Banks'),
    ('Business-to-Business (B2B) Software and Services Startup', 'Business-to-Business (B2B) Software and Services Startup'),
    ('Diagnostic Centre', 'Diagnostic Centre'),
    ('School/College', 'School/College'),
    ('Hospital', 'Hospital'),
    ('IT Enabled Service', 'IT Enabled Service'),
    ('ISP broadband', 'ISP broadband'),
    ('Departmental store', 'Departmental store'),
    ('Developer', 'Developer'),
    ('Agro based firms (incl. Agro Processing/Seed/GM)', 'Agro based firms (incl. Agro Processing/Seed/GM)'),
    ('Travel Agent', 'Travel Agent'),
]

class CompanyDetails(forms.ModelForm):
    are_you_new_entrepreneur = forms.ChoiceField(choices=ENTREPRENEUR_CHOICE, widget=forms.RadioSelect)
    industry_type = forms.MultipleChoiceField(choices=INDUSTRYTYPE_CHOICE, widget=forms.CheckboxSelectMultiple(attrs={}))
    class Meta:
        model = CompanyDetailsInformation
        fields = '__all__'


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']