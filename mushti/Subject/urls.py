
from django.urls import path
from .views import *
app_name = "subject"
urlpatterns =[

    path('', Subject_list_view, name='list_view' ),
    
    path('create/',Subject_create_update_view, name = 'create_view'),
    path('<id>/update/',Subject_create_update_view, name = 'update_view'),
    path('deactivate/',Subject_deactivate_view, name = 'deactivate_view'),
    
    path('<id>/',Subject_detail_view, name = 'detail_view'),


    
]
