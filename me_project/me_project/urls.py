from django.contrib import admin
from django.urls import path, include, re_path
from me_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('account/', include('account.urls')),
    path('join/', views.join, name='join'),
    path('mypage/', views.mypage, name='mypage'),
    path('list/', views.list, name='list'),
    path('new/',views.new,name='new'),
    path('create/', views.create,name='create'),
    path('<str:id>', views.detail, name='detail'),
    re_path(r'^idea/(?P<pk>\d+)/comment/$', views.add_comment_to_idea, name='add_comment_to_idea'),
]
