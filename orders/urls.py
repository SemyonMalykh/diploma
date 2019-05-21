from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'orders'

urlpatterns = [
   path('', views.IndexView, name='index'),
   # path('', views.IndexView.as_view(), name='index'),
   path('opened_orders', views.OpenedOrdersView.as_view(), name = 'opened_orders'),
   path('clients', views.ClientListView.as_view(), name = 'clients'),
   path('client_register', views.ClientRegisterView.as_view(), name = 'client_register'),
   path('geo_temp', views.geo_temp, name = 'geo_temp'),
   url(r'view_order/(?P<id>\d+)', views.view_order, name = 'view_order'),
   url(r'client_edit/(?P<id>\d+)', views.client_edit, name = 'client_edit'),
   url(r'edit_order/(?P<id>\d+)', views.edit_order, name = 'edit_order')
   

]