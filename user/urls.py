from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user),
    path('register/',views.register_user),
    # path('home/',views.home),
]
