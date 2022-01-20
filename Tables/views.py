from django.shortcuts import render
from .models import TableOrder, Table
import datetime
from datetime import timedelta



def order(request):
    date1 = datetime.datetime.today()
    time = datetime.time(10)
    if request.POST:
        try:
            date1 = datetime.datetime.strptime(request.POST.get("datepicker"), "%m/%d/%Y")
        except:
            return render(request, 'Tables/orderTable.html', {'date': "please chose valid date"})
        time = datetime.time(int(request.POST.get("time")))

    orders = list(TableOrder.objects.filter(date=date1))
    orders = list(filter(lambda x: x.time.hour == time.hour, orders))
    occupiedT = []
    for i in orders:
        occupiedT.append(i.tables)
    freeTabels = list(Table.objects.all())
    freeTabels = list(filter(lambda x: x not in occupiedT, freeTabels))
    if date1.date() < datetime.datetime.today().date():
        return render(request, 'Tables/orderTable.html', {'date': "please chose valid date"})
    else:
        return render(request, 'Tables/orderTable.html', {'tables': freeTabels, 'date': date1.strftime("%m/%d/%Y"), "time": time.strftime("%H:%M")})

