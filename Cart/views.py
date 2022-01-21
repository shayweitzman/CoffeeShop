from django.shortcuts import render,redirect
from Cart.models import Cart as Carts
from Menu.models import MenuObj
from decimal import *
def Cart(request):
    msg=''
    if not request.user.is_authenticated:
        sum = 0
        object = MenuObj.objects.filter(id=request.POST.get("menuObjID"))[0]
        print(object)

        if object.lunch:
            sum += round((float(object.price) * 0.8), 2)
        else:
            sum += object.price
        summary = zip([object.name],['1'])
        return render(request, 'Cart/payment.html', {'summary': summary, 'sum': sum, 'msg': msg})

    else:
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
                    if objects[i][0].lunch:
                        sum += round((float(objects[i][0].price)*0.8) * int(quantities[i]),2)
                    else:
                        sum += objects[i][0].price * int(quantities[i])
                if request.user.client.Is_VIP:
                    discount = updateCoffee(request.user.client, orders, quantities)
                    if discount>0:
                        sum -= discount
                        msg = str(discount)+" Discounted from the bill, You are VIP!"
                summary= zip(orders,quantities)
                return render(request, 'Cart/payment.html', {'summary':summary,'sum':sum,'msg':msg})
    return render(request,'Cart/cart.html',{'cart':cart})


def updateCoffee(client,orders,quantities):
    discounts  = 0
    price = 0
    for (objName, quantity) in zip(orders, quantities):
        menuObj = MenuObj.objects.filter(name=objName)[0]
        categories = [c.name for c in menuObj.category.all()]
        if 'Coffee' in categories:
            print(client.coffeeCups)
            client.coffeeCups += int(quantity)
            if client.coffeeCups >= 10:
                discounts = client.coffeeCups//10
                client.coffeeCups = client.coffeeCups - discounts*10
                client.save()
                if menuObj.lunch:

                    price += round((float(menuObj.price) * 0.8) * discounts, 2)
                else:
                    price += discounts * menuObj.price
    return price
