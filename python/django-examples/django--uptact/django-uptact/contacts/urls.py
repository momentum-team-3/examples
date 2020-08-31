"""uptact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_contacts, name="list_contacts"),
    path('add/', views.add_contact, name='add_contact'),
    path('<int:pk>/', views.view_contact, name="view_contact"),
    path('<int:pk>/edit/', views.edit_contact, name='edit_contact'),
    path('<int:pk>/delete/', views.delete_contact, name='delete_contact'),
    path('note/<int:pk>/edit/', views.edit_note, name="edit_note"),
    path('note/<int:c_pk>/<int:pk>/delete/', views.delete_note, name="delete_note"),
    path('note/<int:c_pk>/add/', views.add_note, name="add_note")
]
