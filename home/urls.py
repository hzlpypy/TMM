from django.conf.urls import url

from home import views

urlpatterns = [
    url('page/', views.menu_page),
    url('infor/', views.shop_infor),
    url('add/', views.add_shop),
]
