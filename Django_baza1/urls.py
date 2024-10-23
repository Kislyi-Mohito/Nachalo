from django.contrib import admin
from django.urls import path
from bazaFILENAME import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.info_vb),
    path('login1/', views.login1)
]
