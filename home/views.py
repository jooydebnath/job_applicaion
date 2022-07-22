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


def genarelCategory(request):
    genarel = GenarelCategory()
    genareluser = CreateUser()
    if request.method == 'POST':
        genareluser = CreateUser(request.POST)
        genarel = GenarelCategory(request.POST)
        if genareluser.is_valid() & genarel.is_valid():
            user = genareluser.save()
            genarel = genarel.save(False)
            genarel.user = user
            genarel.save()
        return redirect('login')

    context = {'genarel': genarel, 'genareluser': genareluser}

    return render(request, 'genarel_category.html', context)



def specialSkilledCategory(request):
    return render(request, 'special_skilled_category.html')



def login(request):
    return render(request, 'login.html')