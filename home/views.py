from django.shortcuts import render, redirect
from company.models import *
from . forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group



def home(request):
    return render(request, 'home.html')

@unauthenticated_user
def registerPre(request):
    return render(request, 'register_pre.html')


@unauthenticated_user
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
            group = Group.objects.get(name='employe')
            user.groups.add(group)
        return redirect('login')

    context = {'corporateuser': corporateuser, 'corporate': corporate}
    return render(request, 'corporate_account.html', context)



@unauthenticated_user
def selectCategory(request):
    return render(request, 'select_category.html')


@unauthenticated_user
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
            group = Group.objects.get(name='genarel')
            user.groups.add(group)
        return redirect('login')

    context = {'genarel': genarel, 'genareluser': genareluser}

    return render(request, 'genarel_category.html', context)


@unauthenticated_user
def specialSkilledCategory(request):
    specialcategory = SpecialCategory()
    specialcategoryuser = CreateUser()
    if request.method == 'POST':
        specialcategoryuser = CreateUser(request.POST)
        specialcategory = SpecialCategory(request.POST)
        if specialcategoryuser.is_valid() & specialcategory.is_valid():
            user = specialcategoryuser.save()
            specialcategory = specialcategory.save(False)
            specialcategory.user = user
            specialcategory.save()
            group = Group.objects.get(name='specialskilled')
            user.groups.add(group)
        return redirect('login')

    context = {'specialcategory': specialcategory, 'specialcategoryuser': specialcategoryuser}

    return render(request, 'special_skilled_category.html', context)

@unauthenticated_user
def autismCategory(request):
    autismcategory = AutismCategory()
    autismuser = CreateUser()
    if request.method == 'POST':
        autismuser = CreateUser(request.POST)
        autismcategory = AutismCategory(request.POST)
        if autismuser.is_valid() & autismcategory.is_valid():
            user = autismuser.save()
            autismcategory = autismcategory.save(False)
            autismcategory.user = user
            autismcategory.save()
            group = Group.objects.get(name='autism')
            user.groups.add(group)
        return redirect('login')

    context = {'autismcategory': autismcategory, 'autismuser': autismuser}
    return render(request, 'autism_category.html', context)


@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')