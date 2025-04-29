from django.urls import path
from . import views
urlpatterns = [
    path('', views.MyProfile, name='MyProfile'),
    path('home', views.home, name='home'),
    path('Theform/', views.Theform, name='Theform'),
    path('TheDetails/<int:details_id>', views.TheDetails, name='TheDetails'),
    path('TheEdit/<int:edit_id>', views.TheEdit, name='TheEdit'),
    path('TheRegister/', views.TheRegister, name='TheRegister'),
    path('TheLogin/', views.TheLogin, name='TheLogin'),
    path('TheLogOut/', views.TheLogOut, name='TheLogOut'),
    path('TheDownload/', views.TheDownload, name='TheDownload'),


]
