from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import SignInForm, SignUpForm
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

User = get_user_model()


def signout(request):
    logout(request)
    return redirect("app_account:signin")


class SignUpPage(View):
    # User registration view

    template_name = "app_account/signup.html"
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("app_account:signin")
        context = {"form": forms}
        return render(request, self.template_name, context)
   


class SignInPage(View):
    # User registration view

    template_name = "app_account/signin.html"
    form_class = SignInForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():            
       
            email = request.POST.get('email').lower()
            password = request.POST.get('password')
            
            try:
                user = User.objects.get(email=email)
            except:
                messages.error(request, "User does not exist.")
                
            email = forms.cleaned_data["email"]
            password = forms.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("app_event:calendar")
            else:
                messages.error(request, "Email or password does not exist.")
                
        context = {"form": forms}
        return render(request, self.template_name, context)


class ForgotPasswordPage(View):
    
    template_name = "app_account/forgot-password.html"
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("app_account:signin")
        context = {"form": forms}
        return render(request, self.template_name, context)