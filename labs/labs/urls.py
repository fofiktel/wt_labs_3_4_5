
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('lab_3/', include('lab_3.urls')),
    path('lab_4/', include('lab_4.urls')),
    path('lab_5/', include('lab_5.urls'))
]
