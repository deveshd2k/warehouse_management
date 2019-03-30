from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name="home"),
	path('warehouse_signup',views.warehouse_signup,name="warehouse_signup"),
	path('shop_signup',views.shop_signup,name='shop_signup'),
	path('login',views.login,name="login"),
	path('dashboard',views.dashboard,name="dashboard")
]