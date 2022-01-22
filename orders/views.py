from django.shortcuts import render,redirect
from Authentication.models import Barista
from Menu.models import MenuObj
import json
from orders.models import Order

def myOrders(request):
    if request.POST:
        if "remove" in request.POST:
            print(request.POST.get("remove"))
            order = Order.objects.filter(id=request.POST.get("remove"))
            order[0].delete()
            updateBaristas(-1)
        else:
            order = Order.objects.filter(id=request.POST.get("ready"))
            order[0].delete()
            updateBaristas(-1)
    try:
        if request.user.client:
            orders = Order.objects.filter(client=request.user.client,alreadyPrepared=False)
            numOfOrders = len(orders)
            quantities = [json.loads(q.quatities) for q in orders]
            items = [json.loads(order.menuObjs) for order in orders]
            total = [order.total for order in orders]
    except:
        if request.user.barista or request.user.is_superuser:
            orders = Order.objects.filter(alreadyPrepared=False)
            numOfOrders = len(orders)
            quantities = [json.loads(q.quatities) for q in orders]
            items = [json.loads(order.menuObjs) for order in orders]
            total = [order.total for order in orders]
    return render(request,'Orders/myOrders.html',{'orders':orders,'items':items,'quantities':quantities,'size':range(0,numOfOrders),'total':total})

def PlaceOrder(request):
    if request.POST:
        quantities = request.POST.getlist("quatities")
        orders = request.POST.getlist("orders")
        totalPrice = request.POST.get("sum")
        payMethod = request.POST.get("method")
        orderName = request.POST.get("name")
        updateBought(orders,quantities)
        updateBaristas(1)
        if not request.user.is_authenticated:
            Order.objects.create(client=None,fullname=orderName,paymentMethod= payMethod,menuObjs=json.dumps(orders),quatities=json.dumps(quantities),total=totalPrice,alreadyPrepared=False)
        else:
            Order.objects.create(client=request.user.client, fullname=orderName, paymentMethod=payMethod,
                             menuObjs=json.dumps(orders), quatities=json.dumps(quantities), total=totalPrice,
                             alreadyPrepared=False)
    return redirect('/')

def updateBought(orders,quantities):
    for (objName,quantity) in zip(orders,quantities):
        menuObj = MenuObj.objects.filter(name=objName)[0]
        menuObj.bought += int(quantity)
        menuObj.save()



def updateBaristas(val):
    for barista in Barista.objects.all():
        barista.ordersToPrepare += val
        barista.save()