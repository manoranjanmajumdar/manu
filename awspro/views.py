from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from .models import Services, Users 


# Create your views here.
class home(TemplateView):
    # def get(self, request):
    template_name = 'index.html'


def add_aws_skills(request):
    print('-------python---------')
    if request.method == 'POST':
        description = request.POST.get('description')
        Remarks = request.POST.get('Remarks')
        s_num = request.POST.get('s_num')
        print(Remarks)
        print('########surya########')

        my_model = Services(description=description, Remarks=Remarks, s_num=s_num)
        my_model.save()

        return redirect("add_aws_skills")
    return render(request, 'add_aws_skills.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print("########email", email, password)
        user = Users.objects.get(email=email, password=password)
        print("########user", user)

        if user is not None:
            # login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


# def aws_skillsdata(ListView):
#     model = Services
#     template_name = 'aws_skillsdata.html'
