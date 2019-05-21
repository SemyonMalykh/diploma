from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.mail import send_mail
import datetime
import json

from .forms import OrderRegisterForm, ClientRegisterForm, OrderEditForm
from .models import Client, Order, User, Laundry

def IndexView(request):
    template_name = 'orders/index.html'
    clients = Client.objects.all()

    if request.method == "GET":
        order_form = OrderRegisterForm()
        return render(request, template_name,  {'order_form' :  order_form, })

    if request.method == "POST":
        order = Order()
        order.client = Client.objects.get(id = request.POST['client'])
        order.laundry = Laundry.objects.get(id = request.POST['laundry'])
        order.delivery_date = request.POST['delivery_date_year'] + '-' + request.POST['delivery_date_month'] + '-' + request.POST['delivery_date_day']
        order.price = request.POST['price']
        order.status = request.POST['status']
        order.delivery_time = request.POST['delivery_time']
        order.date_ordered = datetime.date.today()
        order.time_pickup = datetime.datetime.now().time()

        if 'date_payment_year' in request.POST:
            order.date_payment = request.POST['date_payment_year'] + '-' + request.POST['date_payment_month'] + '-' + request.POST['date_payment_day']

        print(request.POST) 
        if 'is_self_pickup' in request.POST:
            order.is_selfpickup = True
            order.delivery_date = None
            order.delivery_time = None
        else:
            order.is_selfpickup = False
        if 'is_paid' in request.POST:
            order.is_paid = True
        else:
            order.is_paid = False
        order.save()
        return HttpResponseRedirect(reverse('orders:opened_orders'))



# class IndexView(generic.ListView):
#     model = Order
#     template_name = 'orders/index.html'

#     def get(self, request):
#         order_form = OrderRegisterForm()
#         return render(request, self.template_name,  {'order_form' :  order_form, })

#     def post(self, request):
#         data = {}
#         # data = dict(request.POST)
#         data['csrfmiddlewaretoken'] = [request.POST['csrfmiddlewaretoken']]
#         data['client'] = [Client.objects.get(id = request.POST['client'])]
#         data['laundry'] = [Laundry.objects.get(id = request.POST['laundry'])]
#         data['delivery_date_month'] = [request.POST['delivery_date_month']]      
#         data['delivery_date_day'] = [request.POST['delivery_date_day']]
#         data['delivery_date_year'] = [request.POST['delivery_date_year']] 
#         data['cost'] = [request.POST['cost']]
#         data['status'] = [request.POST['status']]
#         data['delivery_time'] = [request.POST['delivery_time']]
#         print(request.POST) 
#         order_form = OrderRegisterForm(data)
#         print(data)
#         if order_form.is_valid():
#             order_form.save()
#         else:
#             print('hhmmm')
#         print('Que??')
#         return HttpResponseRedirect(reverse('orders:opened_orders'))

#             csrfmiddlewaretoken
# delivery_date_month
# delivery_date_day
# delivery_date_year
# cost
# client
# laundry
# status
# delivery_time

class ClientRegisterView(generic.ListView):
    template_name = 'orders/client_register.html'

    def get(self, request):
        client_register_form = ClientRegisterForm
        return render(request, self.template_name,  {'client_register_form' :  client_register_form, })

    def post(self, request):
        client_form = ClientRegisterForm(request.POST)
        if(not Client.objects.filter(name = request.POST['name'], second_name = request.POST['second_name'],
                            phone = request.POST['phone'])):
            new_user = User(login = "auto", password = "auto")
            new_user.save()
            new_client = Client(name = request.POST['name'], second_name = request.POST['second_name'], address = request.POST["address"],
                                phone = request.POST['phone'], email = request.POST['email'], user = new_user )
            new_client.save()
        return HttpResponseRedirect(reverse('orders:clients'))


class ClientListView(generic.ListView):
    template_name = 'orders/clients.html'

    def get(self, request):
        client_list = Client.objects.all()
        return render(request, self.template_name,  {'client_list' :  client_list, })

class OpenedOrdersView(generic.ListView):
    template_name = 'orders/opened_orders.html'

    def get(self, request):
        orders_list = Order.objects.all()
        return render(request, self.template_name,  {'orders_list' :  orders_list, })

def geo_temp(request):
    if request.method == "GET":
        orders_list = Order.objects.all()
        return render(request, 'orders/geo_temp.html',  {'orders_list' :  orders_list, })
    if request.method == "POST":
        dist_JSON = request.POST['dist']
        dist = json.loads(dist_JSON)
        print(type(dist))
        dist.sort(key = lambda i: i['addr1'] + i['addr2'])
        for elem in dist:
            print(elem)
        orders_list = Order.objects.all()
        return render(request, 'orders/geo_temp.html',  {'orders_list' :  orders_list, })


def view_order(request, id=None):
    if id:
        order = Order.objects.get(id=id)
        return render(request, 'orders/view_order.html', {'order': order})

def edit_order(request, id=None):
    if request.method == "GET":
        if id:
            order = Order.objects.get(id=id)
            if order.status == 1:
                status = "Заказан"
            elif order.status == 2:
                status = "В обработке"
            elif order.status == 3:
                status = "Готов"
            elif order.status == 4:
                status = "Доставлен"
            if order.delivery_time.minute == 0:
                delivery_time = str(order.delivery_time.hour) + ":" + str(order.delivery_time.minute) + "0"
            else:
                delivery_time = str(order.delivery_time.hour) + ":" + str(order.delivery_time.minute)
            print(type(order.client.id))
            data = {"client" : order.client.name + " " + order.client.second_name,
                    "laundry" : order.laundry.address, "date_ordered" : order.date_ordered,
                    "time_pickup" : order.time_pickup,
                    "delivery_date" : order.delivery_date, "delivery_time" : delivery_time,
                    "is_selfpickup" : order.is_selfpickup, "status" : status, "is_paid" : order.is_paid,
                    "date_payment" : order.date_payment, "price" : order.price}
            order_edit_form = OrderEditForm(data, instance=order) 
            return render(request, 'orders/edit_order.html', {'order_edit_form' : order_edit_form, 'order' : order})
    # if request.method == "POST":
    #     client = Client.objects.get(id=id)
    #     client_form = ClientRegisterForm(request.POST, instance=client)
    #     print(request.POST)
    #     if client_form.is_valid():
    #         client_form.save()
    #         return HttpResponseRedirect(reverse('orders:clients'))

    # laundry = models.ForeignKey(Laundry, on_delete=models.DO_NOTHING)
    # client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # date_ordered = models.DateField()
    # time_pickup = models.TimeField()
    # delivery_date = models.DateField(default="2019-04-11", null=True)
    # delivery_time = models.TimeField(null=True)
    # is_selfpickup = models.BooleanField()
    # status = models.IntegerField()
    # price = models.IntegerField()
    # is_paid = models.BooleanField()
    # date_payment = models.DateField(null=True)

def client_edit(request, id=None):
    if request.method == "GET":
        if id:
            client = Client.objects.get(id=id)
            data = {"name" : client.name, "second_name" : client.second_name, "address" : client.address,
                    "email" : client.email, "gender" : client.gender, "phone" : client.phone}
            client_form = ClientRegisterForm(data, instance=client)
            return render(request, 'orders/client_edit.html', {'client_form' : client_form})
    if request.method == "POST":
        client = Client.objects.get(id=id)
        client_form = ClientRegisterForm(request.POST, instance=client)
        print(request.POST)
        if client_form.is_valid():
            client_form.save()
            return HttpResponseRedirect(reverse('orders:clients'))



# class IndexView(generic.ListView):
#     model = Order
#     template_name = 'orders/index.html'

#     def get(self, request):
#         order_form = OrderRegisterForm()
#         client_form = OrderClientForm()
#         return render(request, self.template_name,  {'client_form' :  client_form, 'order_form' :  order_form, })

#     def post(self, request):
#         order_form = OrderRegisterForm(request.POST)
#         client_form = OrderClientForm(request.POST)
#         #user_name = request.POST['name']
#         if(not Client.objects.filter(name = request.POST['name'], second_name = request.POST['second_name'],
#                             email = request.POST['email'])):
#             new_user = User(login = "auto", password = "auto")
#             new_user.save()
#             #client_form.user = new_user
#             new_client = Client(name = request.POST['name'], second_name = request.POST['second_name'], email = request.POST['email'], user = new_user )
#             #client_form.save()
#             new_client.save()
#         else:
#             client = Client.objects.get(name = request.POST['name'], second_name = request.POST['second_name'], email = request.POST['email'])
#         laundry = Laundry.objects.get(id = 1)
#         is_self_pickup = request.POST.get('is_self_pickup', False)
#         is_payed = request.POST.get('is_payed', False)
#         if is_payed:
#             date_payment = datetime.date.today()
#         else: 
#             date_payment = datetime.date.today()
#         order = Order(laundry = laundry, client =  client, date_ordered = datetime.date.today(), is_selfpickup = is_self_pickup, status = "Ordered", is_paid = is_payed, date_payment = date_payment, time_pickup = '19:00')
#         order.save()
#         return HttpResponseRedirect(reverse('orders:index'))
