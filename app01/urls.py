from django.urls import path
from app01 import views

urlpatterns =[
    path("add_publisher/",views.add_publisher),
    path("publisher_list/",views.publisher_list),
]