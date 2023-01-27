
from django.urls import path
from .views import *
app_name = "classes"
urlpatterns =[

    path('', Classes_list_view, name='list_view' ),
    
    path('create/',Classes_create_update_view, name = 'create_view'),
    path('<id>/update/',Classes_create_update_view, name = 'update_view'),
    path('deactivate/',Classes_deactivate_view, name = 'deactivate_view'),
    
    path('<id>/',Classes_detail_view, name = 'detail_view'),


    
]
