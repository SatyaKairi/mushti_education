
from django.urls import path
from .views import *
app_name = "question"
urlpatterns =[

    path('', Question_list_view, name='list_view' ),
    
    path('create/',Question_create_update_view, name = 'create_view'),
    path('<id>/update/',Question_create_update_view, name = 'update_view'),
    path('deactivate/',Question_deactivate_view, name = 'deactivate_view'),
    
    path('<id>/',Question_detail_view, name = 'detail_view'),


    
]
