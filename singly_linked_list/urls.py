
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home, name='home'),
    path('add_node/',add_node, name='add_node'),
    path('delete_node/',delete_node, name='delete_node'),
    path('insert_at_mid/',insert_at_mid, name='insert_at_mid'),
    path('insert_at_beg/',insert_at_beg, name='insert_at_beg'),
    
]

