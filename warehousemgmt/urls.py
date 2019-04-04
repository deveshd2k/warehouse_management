from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('',views.home,name="home"),
	path('login', auth_views.LoginView.as_view(template_name="login.html"),name = 'login'),
	path('warehouse_signup',views.warehouse_signup,name="warehouse_signup"),
	path('shop_signup',views.shop_signup,name='shop_signup'),
	path('user_login',views.user_login,name="user_login"),
	path('warehouse_dashboard',views.warehouse_dashboard,name="warehouse_dashboard"),
	path('shop_dashboard',views.shop_dashboard,name="shop_dashboard"),
	path('logout',views.userlogout,name="logout"),
	path('photographer_signup',views.photographer_signup,name="photographer_signup"),
	path('photographer_dashboard',views.photographer_dashboard,name='photographer_dashboard')
]