from django.shortcuts import render,redirect
from Cart.models import Cart as Carts
from Menu.models import MenuObj

def Cart(request):
    cart = Carts.objects.filter(client=request.user.client)[0]
    if request.POST:
        if "remove" in request.POST:
            cart.menuObjs.remove(request.POST.get("remove"))
        else:
            sum=0
            objects = [MenuObj.objects.filter(id = i) for i in request.POST.getlist("objects")]
            quantities = request.POST.getlist("quantity")
            orders=[]
            for i in range(len(objects)):
                orders.append(objects[i][0].name)
                sum += objects[i][0].price * int(quantities[i])
            summary= zip(orders,quantities)
            return render(request, 'Cart/payment.html', {'summary':summary,'sum':sum})
    return render(request,'Cart/cart.html',{'cart':cart})


