from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('propietarios', views.propietario_list, name='propietario_list'),

    path('autos', views.auto_list, name='auto_list'),
    path('autos/<int:pk>/', views.detalle_auto, name='detalle_auto'),
    path('autos/new', views.auto_new, name='auto_new'),
    path('autos/<int:pk>/edit/', views.auto_edit, name='auto_edit'),
    

    path('mecanicos', views.mecanico_list, name='mecanico_list'),
    path('trabajos', views.trabajo_list, name='trabajo_list'),
    path('trabajos/<int:pk>/', views.detalle_trabajo, name='detalle_trabajo'),
    path('trabajos/new', views.trabajo_new, name='trabajo_new'),
    path('trabajos/<int:pk>/edit/', views.trabajo_edit, name='trabajo_edit'),
    path('trabajos/delete/<int:pk>', views.trabajo_delete, name='trabajo_delete'),
]