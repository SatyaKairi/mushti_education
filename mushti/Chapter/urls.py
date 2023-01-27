
from django.urls import path
from .views import *
app_name = "chapter"
urlpatterns =[

    path('', Chapter_list_view, name='list_view' ),
    
    path('create/',Chapter_create_update_view, name = 'create_view'),
    path('<id>/update/',Chapter_create_update_view, name = 'update_view'),
    path('deactivate/',Chapter_deactivate_view, name = 'deactivate_view'),
    
    path('<id>/',Chapter_detail_view, name = 'detail_view'),


    
]
