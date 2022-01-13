from django.shortcuts import render
from Menu.models import MenuObj
from django.shortcuts import get_object_or_404

def all_menu(request):
    menu = MenuObj.objects.all()
    return render(request, 'menu/all_menu.html', {'menu': menu})


def sort(request):
    menu = get_object_or_404(MenuObj, pk=1)
    return render(request, 'menu/sorted.html', {'print': request.path})
