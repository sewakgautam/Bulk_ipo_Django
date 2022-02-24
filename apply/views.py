import imp
from pyexpat import model
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView , ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import *
from .models import *
# Create your views here.

class Index(LoginRequiredMixin, TemplateView):
    template_name = 'apply/index.html'
    login_url = '/login/'

class Login(FormView):
    template_name = 'apply/login.html'
    redirect_authenticated_user = True
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super(Login, self).dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        form = Logins(request.POST)
        if form.is_valid():
            u_name = form.cleaned_data['Username']
            passd = form.cleaned_data['Password']
            person = authenticate(username= u_name, password=passd)
            if person is not None:
                login(request, person)
                return redirect('index')
            return HttpResponse("Invalid Credentials")
    def get(self, request, *args, **kwargs):
        form = Logins()
        return render(request, 'apply/login.html', {'login_data':form})


class Signup(TemplateView):
    template_name = 'apply/signup.html'
    redirect_authenticated_user = True
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super(Login, self).dispatch(request, *args, **kwargs)

def Logout(request):
    logout(request)
    return redirect('index')

class Details(TemplateView):
    template_name = 'apply/details.html'

class Add(FormView):
    template_name = 'apply/add_dmat.html'
    def post(self, request, *args, **kwargs):
        form = Dmat(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Name']
            boid = form.cleaned_data['Boid']
            crn = form.cleaned_data['Crn']
            kitta = form.cleaned_data['Apply']
            pin = form.cleaned_data['Pin']
            Insert_data = AddAccount.objects.create(Name=name, Boid=boid, Apply_kitta=kitta, Crn=crn, Pin=pin)
            if Insert_data is not None:
                return redirect('profile')
            return HttpResponse("Please Insert all valid Input Fields")
    def get(self, request, *args, **kwargs):
        form = Dmat()
        return render(request, 'apply/add_dmat.html' , {'add_account':form} )


class Profile(ListView):
    template_name = 'apply/profile.html'
    model = AddAccount
    context_object_name = 'dmat'

class Ipocheck(TemplateView):
    template_name = 'apply/ipocheck.html'

class EditBoid(TemplateView):
    template_name = 'apply/edit.html'