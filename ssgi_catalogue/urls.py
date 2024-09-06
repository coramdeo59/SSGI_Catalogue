from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sidebarquery.urls')),
    path('authenticate/', include('authenticate.urls')),
    path('payments/', include('payments.urls')),
    path('bookmarks/', include('bookmarks.urls')),
]

urlpatterns += staticfiles_urlpatterns()
