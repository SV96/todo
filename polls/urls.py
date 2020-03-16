from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_add', views.new_add, name='new_add'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('update_todo/<int:todo_id>/edit/', views.edit_todo, name='edit_todo'),
    path('update_todo/<int:todo_id>/', views.update_todo, name='update_todo'),
    path('detail_todo/<int:todo_id>/', views.detail_todo, name='detail_todo'),

]
