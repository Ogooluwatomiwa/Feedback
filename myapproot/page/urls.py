from django.contrib import admin
from django.urls import path, include
from page import views

urlpatterns = [
    path('page/', views.page, name='page'),
    path('admin/', admin.site.urls),
]