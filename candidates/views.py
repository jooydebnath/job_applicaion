from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home . decorators import *

@login_required()
@allowed_users(allowed_roles=['genarel'])
def candidateDashboard(request):
    return render(request, 'candidate.html')

@login_required()
@allowed_users(allowed_roles=['specialskilled'])
def specialCategory(request):
    return render(request, 'special_category.html')

@login_required()
@allowed_users(allowed_roles=['autism'])
def autismCategory(request):
    return render(request, 'special_category.html')