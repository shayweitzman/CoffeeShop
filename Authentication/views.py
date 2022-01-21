from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm,BaristaProfileForm,ClientProfileForm
from Cart.models import Cart
from orders.models import unPreparedOrders


# def signupuser(request):
#     if request.method == 'POST':
#         ans = request.POST.get('kinduser')
#         if ans == '1':
#             return studentsignupuser(request)
#
#         elif ans == '2':
#             return adultsignupuser(request)
#         else:
#             return redirect("homepage")
#
#     else:
#         return render(request, 'authentication/signup2.html')

def AddClient(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = ClientProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            Cart.objects.create(client=user.client)
            return redirect("homepage")
    else:
        form = ExtendedUserCreationForm()
        profile_form= ClientProfileForm()
    if "clicked" in request.POST:
        return render(request, 'Authentication/AddClient.html', {'form': form, 'profile_form': profile_form, 'error': "Bad Data Please Try Again"})
    context= {'form': form, 'profile_form':profile_form,'error': ""}
    return render(request, 'Authentication/AddClient.html', context)
def AddBarista(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = BaristaProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            user.barista.ordersToPrepare = unPreparedOrders
            login(request, user)
            return redirect("homepage")
    else:
        form = ExtendedUserCreationForm()
        profile_form= BaristaProfileForm()
    if "clicked" in request.POST:
        return render(request, 'Authentication/AddBarista.html', {'form': form, 'profile_form': profile_form, 'error': "Bad Data Please Try Again"})
    context= {'form': form, 'profile_form':profile_form,'error': ""}
    return render(request, 'Authentication/AddBarista.html', context)


def logoutuser(request):
    logout(request)
    return redirect('homepage')



def loginU(request):
    if request.method == 'GET':
        return render(request, 'Authentication/Login.html', {'form': AuthenticationForm(), 'error': ""})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'Authentication/Login.html', {'form': AuthenticationForm(), 'error': "Wrong username or password"})
        else:
            login(request, user)
            return redirect('homepage')