from django.urls import path
from .views import catalog_content, create_catalog, rename_catalog, delete_catalog,copy_file,read_file

urlpatterns = [
    path('catalog_content/', catalog_content),
    path('create_catalog/', create_catalog),
    path('rename_catalog/', rename_catalog),
    path('delete_catalog/', delete_catalog),
    path('rename_file/', rename_catalog),
    path('copy_file/', copy_file),
    path('delete_file/', delete_catalog),
    path('read_file/', read_file),

]