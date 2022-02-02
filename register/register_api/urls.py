from django.urls import path
from .views import api_detail_view, api_update_view, api_delete_view,api_create_view,ApiRegisterView


app_name='crud_api'
urlpatterns = [
    path('detail/api/<str:pk>', api_detail_view, name='register_home_api' ),
    path('update/api/<str:pk>', api_update_view, name='register_update_api' ),
    path('delete/api/<str:pk>', api_delete_view, name='register_delete_api' ),
    path('create/api', api_create_view, name='register_create_api' ),
    path('registers/api', ApiRegisterView.as_view(), name='register_list_api' ),
]