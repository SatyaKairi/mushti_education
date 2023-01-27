
from django.urls import path
from .views import *
app_name = "exercise"
urlpatterns =[

    path('', Exercise_list_view, name='list_view' ),
    
    path('create/',Exercise_create_update_view, name = 'create_view'),
    path('<id>/update/',Exercise_create_update_view, name = 'update_view'),
    path('deactivate/',Exercise_deactivate_view, name = 'deactivate_view'),
    
    path('<id>/',Exercise_detail_view, name = 'detail_view'),


    
]
