
from django.contrib import admin
from django.urls import path
from appOne import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send/',views.SendMailView.as_view(),name='send-email')
]
