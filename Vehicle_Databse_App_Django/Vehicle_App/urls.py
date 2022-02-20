from django.urls import path
from . import views

app_name = 'Vehicle_App'

urlpatterns = [
    path('', views.VehicleList.as_view(), name = 'vehicle_list'),
    path('<int:pk>/', views.VehicleDetail.as_view(), name='vehicle_detail'),
    path('create_vehicle/', views.VehicleCreate.as_view(), name='vehicle_creation'),
    path('<int:pk>/update_vehicle/', views.VehicleUpdate.as_view(), name ='vehicle_update'),
    path('<int:pk>/delete_vehicle/', views.VehicleDelete.as_view(), name ='vehicle_delete'),
]


