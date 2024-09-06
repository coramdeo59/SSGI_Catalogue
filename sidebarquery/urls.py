# from django.urls import path, include
# from . import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# from .views import SSGIListView, SSGIRetrieveView, SSGICreateView, SSGISearchView,footprint_view


# urlpatterns = [
 
#  path('search_page', views.get, name="fill_form"),
# #  path('fill_form', SearchForm.as_view(), name="fill_form"),
# #  path('result',views.form,name='form'),  
 
# path('about', views.display_html, name='about_us'),
# path('', views.home, name='home'),

 
#  path('serve_lat_long/',views.serve_lat_long,name='serve_lat_long'),
#  path('feedback', views.feedback_view, name='feedback'),
#  path('serve_image/', views.serve_image, name='serve_image'),
 
#  path('download_zip/', views.download_zip, name='download_zip'),
#  path('footprint/<int:id>/', views.footprint_view, name='footprint'),

# path('api-auth/', include('rest_framework.urls')),
#  path('api/accounts/', include('accounts.urls')),
#  path('api/token/', TokenObtainPairView.as_view(), name='obtain-token-pair'),
#  path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),

# path('api/ssgi/', SSGIListView.as_view(),name='api-ssgi-all'),
# path('api/ssgi/new/', SSGICreateView.as_view(),name='api-ssgi-new'),
# path('api/ssgi/search/', SSGISearchView.as_view(),name='api-ssgi-search'),
# path('api/ssgi/<int:pk>/', SSGIRetrieveView.as_view() ,name='api-ssgi-single'),

# ]

from django.urls import path
from . import views

# from .views import SearchForm


urlpatterns = [
 
 path('search_page', views.get, name="fill_form"),
#  path('fill_form', SearchForm.as_view(), name="fill_form"),
#  path('result',views.form,name='form'),  
 
path('about', views.display_html, name='about_us'),
path('', views.home, name='home'),

 
 path('serve_lat_long/',views.serve_lat_long,name='serve_lat_long'),
 path('feedback', views.feedback_view, name='feedback'),
 path('serve_image/<str:path>/', views.serve_image, name='serve_image'),
 
 path('download_zip/<str:dir_path>/', views.download_zip, name='download_zip'),
]

