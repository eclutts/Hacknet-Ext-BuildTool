from django.urls import path

from . import views

app_name = 'nodebuilder'
urlpatterns = [
    path('', views.obj_list, name='obj_list'),
    path('addObj/<int:type>/<int:subtype>/', views.add_obj, name='add_obj'),
    path('<str:obj_sql_id>/', views.view_obj, name='view_obj'),
    path('gen_obj/<str:obj_sql_id>/', views.gen_obj, name='gen_obj'),
    path('download_obj/<str:obj_sql_id>/', views.download_obj, name='download_obj'),
]