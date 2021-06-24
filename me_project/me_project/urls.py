from django.contrib import admin
from django.urls import path, include, re_path
from me_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('account/', include('account.urls')),
    path('join/', views.join, name='join'),
    path('mypage/', views.mypage, name='mypage'),
    path('myinfo/',views.myinfo,name='myinfo'),
    path('myq/',views.myq,name='myq'),
    path('myc/',views.myc,name='myc'),
    path('list/', views.list, name='list'),
    path('new/',views.new,name='new'),
    path('create/', views.create,name='create'),
    path('<str:id>', views.detail, name='detail'),
    path('idea/<int:idea_id>/comment/', views.add_comment_to_idea, name='add_comment_to_idea'),
]
