from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import TableOrder, Table
from django.shortcuts import get_object_or_404
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def createOrder(request, table_id, time, date):
    messages.warning(request, "Are you shore you whant to order the table to" + date + time, False)
    table = get_object_or_404(Table, pk=table_id)
    try:
        TableOrder.objects.create(clients=request.user.client, tables=table, time=time,
                              date=date.split('/')[2] + '-' + date.split('/')[0] + '-' + date.split('/')[1])
    except:
        return 0
    return 1



@login_required
def order(request):
    date1 = datetime.datetime.today()
    time = datetime.time(datetime.datetime.today().hour + 1)
    if "reserved" in request.POST:
        if(not createOrder(request, request.POST.get("reserved"), request.POST.get("time"), request.POST.get("date"))):
            return HttpResponseRedirect("/Error the order didn't saverd/")
        else:
            return render(request, "Tables/table_resevation.html")
    elif request.POST:
        try:
            date1 = datetime.datetime.strptime(request.POST.get("datepicker"), "%m/%d/%Y")
        except:
            return render(request, 'Tables/orderTable.html',
                          {'date': date1.strftime("%m/%d/%Y"), 'time': "please chose valid date"})
        time = datetime.time(int(request.POST.get("time")))

    orders = list(TableOrder.objects.filter(date=date1))
    orders = list(filter(lambda x: x.time.hour == time.hour, orders))
    occupiedT = []
    for i in orders:
        occupiedT.append(i.tables)
    freeTabels = list(Table.objects.all())
    freeTabels = list(filter(lambda x: x not in occupiedT, freeTabels))
    if date1.date() < datetime.datetime.today().date():
        return render(request, 'Tables/orderTable.html',
                      {'date': date1.strftime("%m/%d/%Y"), 'time': "please chose valid date"})
    elif date1.date() == datetime.datetime.today().date() and time.hour <= datetime.datetime.today().hour:
        return render(request, 'Tables/orderTable.html',
                      {'date': date1.strftime("%m/%d/%Y"), 'time': "please chose valid time"})
    else:
        return render(request, 'Tables/orderTable.html',
                      {'tables': freeTabels, 'date': date1.strftime("%m/%d/%Y"), "time": time.strftime("%H:%M")})
