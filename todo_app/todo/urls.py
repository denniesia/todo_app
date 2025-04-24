from django.urls import path
from .views import sign_up_view, home_view, login_view, todo_view, edit_todo_view, delete_todo_view, signout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', sign_up_view, name='sign_up'),
    path('login/', login_view, name='login'),
    path('todo_page/', todo_view, name='todo'),
    path('edit/<int:id>/', edit_todo_view, name='edit_todo'),
    path('delete/<int:id>/', delete_todo_view, name='delete-todo'),
    path('signout/', signout_view, name='signout'),
]


