from django.shortcuts import render, redirect
from account.forms import SubscriberForm, RegistrationForm, LoginForm, ChangePasswordFrom
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import  reverse_lazy
from django.contrib import messages
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import  get_user_model
from account.tasks import send_confirmation_mail
from account.tools.tokens import account_activation_token
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # http://example.com
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https
            send_confirmation_mail(user_id=user.id, site_address=site_address)
            messages.success(request, 'Siz ugurla qeydiyyatdan kecdiniz')
            return redirect(reverse_lazy('home:home'))
    context = {
        'form': form
    }

    return render(request, 'registration/login.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('home:home'))
    elif user:
        messages.error(request, 'Email is not activated. May be is already activated')
        return redirect(reverse_lazy('account:register'))
    else:
        messages.error(request, 'Email is not activated')
        return redirect(reverse_lazy('account:register'))


def account(request):
    return render(request, 'my-account.html')

def subscriber(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, "./includes/footer.html", context)


class LoginView(TemplateView):
    template_name = 'registration/login.html'

# def login(request):
#     next_page = request.GET.get('next')  # /admin/stories/recipe/1/change/1
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=email, password=password)
#             if user:
#                 django_login(request, user)
#                 messages.success(request, 'Siz ugurla daxil oldunuz')
#                 if next_page:
#                     return redirect(next_page)
#                 return redirect(reverse_lazy('home:home'))
#             else:
#                 messages.success(request, 'Daxil etdiyiniz melumatlar yalnisdir')
#     context = {
#         'login_form': form
#     }
#     return render(request, 'registration/login.html', context)


class LogoutView(LoginRequiredMixin, APIView):
    def get(self, request, format=None):
        django_logout(request)
        messages.success(request, 'Siz cixish etdiniz.')
        return Response({'message':"Siz cixish etdiniz."})


@login_required
def change_password(request):
    form = ChangePasswordFrom()
    if request.method == 'POST':
        form = ChangePasswordFrom(data=request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get("password1")
            if not request.user.check_password(password1):
                messages.success(request, 'Password and User password is not same')
                return redirect(reverse_lazy('account:change_password'))
            password2 = form.cleaned_data.get("password2")
            password3 = form.cleaned_data.get("password3")
            if password2 != password3:
                messages.success(request, 'Password and Confirm password is not same')
                return redirect(reverse_lazy('account:change_password'))
            request.user.set_password(form.cleaned_data.get('password2'))
            request.user.save()
        messages.success(request, 'Password ugurla deyisdirildi...')  
        return redirect(reverse_lazy('account:login'))

    context = {
        'form': form
    }
    return render(request, 'change_password.html', context)
