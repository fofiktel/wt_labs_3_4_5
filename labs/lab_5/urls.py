from django.urls import path
from .views import catalog_content, create_catalog, rename_catalog

urlpatterns = [
    path('catalog_content/', catalog_content),
    path('create_catalog/', create_catalog),
    path('rename_catalog/', rename_catalog)

]