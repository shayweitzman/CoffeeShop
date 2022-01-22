from django.shortcuts import render, redirect
from Authentication.models import Barista
from Menu.models import MenuObj
import json
from orders.models import Order
from Tables.models import TableOrder
import datetime
from .forms import TableOrderForm
from django.shortcuts import get_object_or_404
from Cart.models import Cart as Carts


def myOrders(request):
    if request.POST:
        if "remove" in request.POST:
            order = Order.objects.filter(id=request.POST.get("remove"))
            order[0].delete()
            updateBaristas(-1)
        else:
            order = Order.objects.filter(id=request.POST.get("ready"))
            order[0].delete()
            updateBaristas(-1)
    try:
        if request.user.client:
            orders = Order.objects.filter(client=request.user.client, alreadyPrepared=False)
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
    return render(request, 'Orders/myOrders.html',
                  {'orders': orders, 'items': items, 'quantities': quantities, 'size': range(0, numOfOrders),
                   'total': total})


def TableOrders(request):
    orders = list(TableOrder.objects.all())
    orders = TableOrder.objects.order_by('date')
    orders = list(filter(lambda x: x.date > datetime.date.today(), orders))

    return render(request, 'orders/tableOrders.html', {'orders': orders})


def editTorder(request, table_id):
    msg =''
    currentOrder = get_object_or_404(TableOrder, pk=table_id)
    if request.method == "GET":
        return render(request, "Orders/editTableOrder.html", {"form": TableOrderForm(instance=currentOrder)})
    elif request.method == "POST":
        if "delete" in request.POST:
            TableOrder.delete(currentOrder)
            return redirect("table_orders")
        else:
            form = TableOrderForm(request.POST)
            if form.is_valid():
                TableOrder.delete(currentOrder)
                newOrder = form.save(commit=False)
                newOrder.save()
                return redirect("table_orders")
            else:
                msg = 'Error while trying to save! Nothing saved.'
                return render(request, "Orders/editTableOrder.html", {"form": TableOrderForm(instance=currentOrder),"msg":msg})
    return redirect("table_orders")


def PlaceOrder(request):
    if request.POST:
        summary=request.POST.getlist("summary")
        quantities = []
        orders= []
        for i in summary:
            q,o = i.split('$')
            quantities.append(str(q))
            orders.append(str(o))
        totalPrice = request.POST.get("sum")
        payMethod = request.POST.get("method")
        orderName = request.POST.get("name")
        updateBought(orders,quantities)
        updateBaristas(1)
        if not request.user.is_authenticated:
            Order.objects.create(client=None,fullname=orderName,paymentMethod= payMethod,menuObjs=json.dumps(orders),quatities=json.dumps(quantities),total=totalPrice,alreadyPrepared=False)
        else:
            cart = Carts.objects.filter(client=request.user.client)[0]
            cart.menuObjs.clear()
            Order.objects.create(client=request.user.client, fullname=orderName, paymentMethod=payMethod,
                             menuObjs=json.dumps(orders), quatities=json.dumps(quantities), total=totalPrice,
                             alreadyPrepared=False)

    return redirect('/')


def updateBought(orders, quantities):
    for (objName, quantity) in zip(orders, quantities):
        menuObj = MenuObj.objects.filter(name=objName)[0]
        menuObj.bought += int(quantity)
        menuObj.save()


def updateBaristas(val):
    for barista in Barista.objects.all():
        barista.ordersToPrepare += val
        barista.save()
