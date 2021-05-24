# Use include() to add paths from the catalog application
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('catalog/', views.home, name='home'),
    path('reghosp/', views.registerhosp, name='registerhosp'),
    path('regdonor/', views.registerdonor, name='registerdonor'),
    path('login/', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
    
    path('hospital/', views.hospital, name='hospital'), 
    path('donorlist/',views.donorlist, name='donorlist'),

    path('scheduledonation/', views.scheduledonation, name='scheduledonation'),
    path('contacthosp/',views.contacthosp, name='contacthosp'),
    path('contactdonor/',views.contactdonor, name='contactdonor'),    

    path('hospitalprofile/<str:id>/', views.hospitalprofile, name='hospitalprofile'),
    path('donorprofile/<str:id>/',views.donorprofile, name='donorprofile'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="catalog/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="catalog/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="catalog/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="catalog/password_reset_done.html"),name="password_reset_complete"),

]
