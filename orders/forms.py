from django import forms
from .models import Order, Client, Laundry
import datetime
from django.utils import timezone

MONTHS = {
    1:('Январь'), 2:('Февраль'), 3:('Март'), 4:('Апрель'),
    5:('Май'), 6:('Июнь'), 7:('Июль'), 8:('Август'),
    9:('Сентябрь'), 10:('Октябрь'), 11:('Ноябрь'), 12:('Декабрь')
    }

def gen_times(): 
    open_time = datetime.time(14,0)
    close_time = datetime.time(19,0)
    time_list = []
    tmp_time_list = []
    tmp_time = datetime.datetime.now() #datime.datime provides timedelta instead of datetime.time
    tmp_time = tmp_time.replace(hour = open_time.hour, minute = open_time.minute,second = 0, microsecond= 0)
    while(tmp_time.time() <= close_time):
        time_list.append(tmp_time.time())
        tmp_time += datetime.timedelta(minutes = 30)
    for time in time_list:
        minutes = str(time.minute)
        if (len(minutes) == 1):
            minutes = '0' + minutes
        hours = str(time.hour)
        tmp_time_list.append(tuple((hours + ':' + minutes, 
                                    hours + ':' + minutes)))
    return (tuple(tmp_time_list))


    #     laundry = models.ForeignKey(Laundry, on_delete=models.DO_NOTHING)
    # client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # date_ordered = models.DateField()
    # time_pickup = models.TimeField()
    # delivery_date = models.DateField(default="2019-04-11")
    # delivery_time = models.TimeField()
    # is_selfpickup = models.BooleanField()
    # status = models.CharField(max_length=200)
    # price = models.IntegerField()
    # is_paid = models.BooleanField()
    # date_payment = models.DateField()

def gen_status():
    status_list = []
    status_list.append((1, "Заказан"))
    status_list.append((2, "В обработке"))
    status_list.append((3, "Готов"))
    status_list.append((4, "Доставлен"))
    return status_list
    
def gen_clients():
    clients = Client.objects.all()
    client_list = []
    for client in clients:
        client_list.append((client.id, client.name + " " + client.second_name))
    return tuple(client_list)

def gen_laundromats():
    laundromats = Laundry.objects.all()
    laundry_list = []
    for laundry in laundromats:
        laundry_list.append((laundry.id, laundry.address))
    return tuple(laundry_list)

class OrderRegisterForm(forms.ModelForm):
    CLIENTS = gen_clients()
    TIMES = gen_times()
    client = forms.TypedChoiceField(label='Клиент', choices = CLIENTS)
    laundry = forms.TypedChoiceField(label='Прачечная', choices = gen_laundromats())
    date_ordered = forms.DateField(label='Дата принятия',  widget = forms.SelectDateWidget(months=MONTHS),  initial=timezone.now(), disabled=True)
    is_self_pickup = forms.BooleanField(label = 'Самовывоз',required=False, initial=False)
    delivery_date = forms.DateField(label='Дата доставки', widget = forms.SelectDateWidget(months=MONTHS), initial=timezone.now())
    delivery_time = forms.ChoiceField(label='Время доставки', choices = TIMES)
    price = forms.IntegerField(label='Стоимость заказа', min_value = 0)
    status = forms.ChoiceField(label='Статус', choices = gen_status(), initial=(2, "В обработке"))
    is_paid = forms.BooleanField(label = 'Оплачен', required=False, initial=False)
    date_payment = forms.DateField(label='Дата оплаты',  widget = forms.SelectDateWidget(months=MONTHS),  initial=timezone.now(), disabled=True)
    class Meta:
        model = Order
        fields = ('client', 'laundry' , 'date_ordered', 'is_self_pickup', 'delivery_date',
                  'delivery_time', 'status', 'price', 'is_paid', 'date_payment')

class OrderEditForm(forms.ModelForm):
    TIMES = gen_times()
    client = forms.TypedChoiceField(label='Клиент', choices = gen_clients(), disabled=True)
    laundry = forms.TypedChoiceField(label='Прачечная', choices = gen_laundromats())
    date_ordered = forms.DateField(label='Дата принятия',  widget = forms.SelectDateWidget(months=MONTHS),  initial=timezone.now(), disabled=True)
    is_self_pickup = forms.BooleanField(label = 'Самовывоз',required=False, initial=False)
    delivery_date = forms.DateField(label='Дата доставки', widget = forms.SelectDateWidget(months=MONTHS), initial=timezone.now())
    delivery_time = forms.ChoiceField(label='Время доставки', choices = TIMES)
    price = forms.IntegerField(label='Стоимость заказа', min_value = 0)
    status = forms.ChoiceField(label='Статус', choices = gen_status(), initial=(2, "В обработке"))
    is_paid = forms.BooleanField(label = 'Оплачен', required=False, initial=False)
    date_payment = forms.DateField(label='Дата оплаты',  widget = forms.SelectDateWidget(months=MONTHS),  initial=timezone.now(), disabled=True)
    class Meta:
        model = Order
        fields = ('client', 'laundry' , 'date_ordered', 'is_self_pickup', 'delivery_date',
                  'delivery_time', 'status', 'price', 'is_paid', 'date_payment')


class ClientRegisterForm(forms.ModelForm):
   name = forms.CharField(label='Имя')
   second_name = forms.CharField(label= 'Фамилия')
   email = forms.EmailField(label='Email', required = False)
   gender = forms.ChoiceField(label='Пол', choices = [(False, 'Мужской'), (True, 'Женский')])
   address = forms.CharField(label='Адрес', required = False)
   phone = forms.CharField(label='Телефон', required = False)
   class Meta:
        model = Client
        fields = ('name', 'second_name', 'phone','email', 'address', 'gender')

class OrderEditForm(forms.ModelForm):
    MONTHS = {
        1:('Январь'), 2:('Февраль'), 3:('Март'), 4:('Апрель'),
        5:('Май'), 6:('Июнь'), 7:('Июль'), 8:('Август'),
        9:('Сентябрь'), 10:('Октябрь'), 11:('Ноябрь'), 12:('Декабрь')
        }
    #date = forms.DateField(label='Дата посещения', widget = forms.SelectDateWidget(months=MONTHS))
    #num_users_registred = forms.IntegerField(label='Количество посетителей (не более 10)', min_value = 1, max_value = 10)
    TIMES = gen_times()
    is_self_pickup = forms.BooleanField(label = 'Самовывоз', required=False)
    delivery_date = forms.DateField(label='Дата доставки', widget = forms.SelectDateWidget(months=MONTHS))
    delivery_time = forms.ChoiceField(label='Время доставки', choices = TIMES)
    price = forms.IntegerField(label='Стоимость заказа', min_value = 0)
    is_payed = forms.BooleanField(label = 'Оплачен', required=False)
    class Meta:
        model = Order
        fields = ('is_self_pickup', 'delivery_date', 'delivery_time', 'price', 'is_payed')