from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('<str:content_id>', detail, name="detail"),
    path('new/', new, name="new"),
    #path('create/', new, name="new"),
    path('edit/<str:id>', edit, name="edit"),
    #path('update/<str:id>', edit, name="edit"),
    path('delete/<str:id>', delete, name="delete"),
    path('animals/', animals, name="animals"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)