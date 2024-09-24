
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home),
    path("test/",views.testpage),
    path('predict/',views.result,name="res"),
    path("",include(('user.urls','user'),"user")),
    path('contact/',views.contact),


]
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
