from django.shortcuts import render
from Menu.models import MenuObj, categoryMenu
from django.shortcuts import get_object_or_404

def all_menu(request):
    menu = MenuObj.objects.all()
    categiries = categoryMenu.objects.all()
    return render(request, 'menu/all_menu.html', {'menu': menu, 'categiries': categiries})


def sort(request):
    menu = MenuObj.objects.all()
    categiries = categoryMenu.objects.all()
    if 'HTL' in request.path:
        menu = MenuObj.objects.order_by('-price')
    elif 'LTH' in request.path:
        menu = MenuObj.objects.order_by('price')
    elif 'DOTD' in request.path:
        menu = MenuObj.objects.filter(DOTD=True)[:5]
    elif 'popularity' in request.path:
        menu = MenuObj.objects.order_by('-bought')


    return render(request, 'menu/all_menu.html', {'menu': menu, 'categiries': categiries, 'print': request.path})
