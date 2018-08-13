from django.urls import path

from . import views


app_name = 'guestbook'

urlpatterns = [
    path('', views.GuestbookView.as_view(), name='index'),
    path('add/', views.GuestbookCreateView.as_view(), name='add'),
    path('<int:pk>/delete/', views.GuestbookDeleteView.as_view(), name='delete')
]
