from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.register, name='registration'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('home/', views.home_page, name='home'),
    path('add_note/', views.add_note, name='add_note'),
    path('notes/', views.notes_page, name='notes'),
]
