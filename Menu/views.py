from django.shortcuts import render
from Menu.models import MenuObj, categoryMenu


def all_menu(request):
    menu = MenuObj.objects.all()
    categiries = categoryMenu.objects.all()
    return render(request, 'menu/all_menu.html', {'menu': menu, 'categiries': categiries})


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
