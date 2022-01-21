from django.shortcuts import render
from Menu.models import MenuObj, categoryMenu
from django.shortcuts import get_object_or_404
from Cart.models import Cart
from Authentication.models import Client
from datetime import date


def all_menu(request):
    msg = ''
    if request.method == "POST":
        cart = Cart.objects.filter(client=request.POST.get("userID"))[0]
        menuObj = MenuObj.objects.filter(id=request.POST.get("menuObjID"))[0]
        if menuObj in cart.menuObjs.all():
            msg = 'Product already in your cart!'
        else:
            msg = 'Product added successfully!'
            cart.menuObjs.add(menuObj)
    menu = MenuObj.objects.all()
    if request.user.is_authenticated:
        try:
            age = calcAge(request.user.client.birthday)
            if age<18:
                menu = MenuObj.objects.filter(ageLimitation=False)
        except:
            pass
    elif not request.user.is_authenticated:
        menu = MenuObj.objects.filter(ageLimitation=False)
    categiries = categoryMenu.objects.all()
    return render(request, 'menu/all_menu.html', {'menu': menu, 'categiries': categiries,'msg':msg})

def calcAge(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def sort(request):
    menu = MenuObj.objects.all()
    categiries = categoryMenu.objects.all()
    for categry in categiries:
        if categry.name in request.path:
            menu = MenuObj.objects.filter(category=categry)
    if 'HTL' in request.path:
        menu = MenuObj.objects.order_by('-price')
    elif 'LTH' in request.path:
        menu = MenuObj.objects.order_by('price')
    elif 'DOTD' in request.path:
        menu = MenuObj.objects.filter(DOTD=True)[:5]
    elif 'popularity' in request.path:
        menu = MenuObj.objects.order_by('-bought')
    elif 'VIP' in request.path:
        menu = MenuObj.objects.filter(VIP=True)
    elif 'morning' in request.path:
        menu = MenuObj.objects.filter(morning=True)
    elif 'lunch' in request.path:
        menu = MenuObj.objects.filter(lunch=True)
    elif 'evning' in request.path:
        menu = MenuObj.objects.filter(evning=True)
    elif 'availability' in request.path:
        menu = MenuObj.objects.filter(availability=True)
    elif 'limitation' in request.path:
        menu = MenuObj.objects.filter(ageLimitation=True)


    return render(request, 'menu/all_menu.html', {'menu': menu, 'categiries': categiries})
