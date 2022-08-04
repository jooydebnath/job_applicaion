from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home . decorators import *


@login_required()
@allowed_users(allowed_roles=['corporate'])
def corporateDashboard(request):
    return render(request, 'corporate_dashboard.html')

@login_required()
@allowed_users(allowed_roles=['corporate'])
def corporateProfile(request):
    return render(request, 'profile.html')