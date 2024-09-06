from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/',views.bookmark_image, name='bookmark' ),
    path('', views.bookmark_list, name='bookmark-list')
]
         