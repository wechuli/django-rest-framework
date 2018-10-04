from django.urls import path
from .views import polls_list,polls_detail

urlpatterns = [

    path("",polls_list,name="polls_list"),
    path("<int:pk>/",polls_detail,name="polls_detail"),
   
]