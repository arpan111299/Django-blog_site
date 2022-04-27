from django.shortcuts import render
from django.views import *
from django.views.generic import *

# Create your views here.
class LoginAdminView(View):
    def get(self,request):
        if request.user.is_superuser:
            return render(request, 'dashboard-customadmin.html')
        else:
            return render(request, 'login-customadmin.html')