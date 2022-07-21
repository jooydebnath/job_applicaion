from django.shortcuts import render, redirect
from company.models import *
from . forms import *
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def registerPre(request):
    return render(request, 'register_pre.html')

def corporateRegister(request):
    corporate = CompanyDetails()
    corporateuser = CreateUser()
    if request.method == 'POST':
        corporateuser = CreateUser(request.POST)
        corporate = CompanyDetails(request.POST)
        if corporateuser.is_valid() & corporate.is_valid():
            user = corporateuser.save()
            corporate = corporate.save(False)
            corporate.user = user
            corporate.save()
        return redirect('login')

    context = {'corporateuser': corporateuser, 'corporate': corporate}
    return render(request, 'corporate_account.html', context)

def selectCategory(request):
    return render(request, 'select_category.html')


def login(request):
    return render(request, 'login.html')