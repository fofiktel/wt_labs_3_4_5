from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
import os
from rest_framework.response import Response

ROOT_PATH = "D:\Programming\pythonProjects\wt_labs\\"

@api_view(['GET'])
def catalog_content(request):
    dirs = []
    with os.scandir("D:\Programming\pythonProjects\wt_labs") as it:
        for entry in it:
            if entry.is_dir() and entry.name != '.idea':
                dirs.append(entry.name)

    return Response({"1": dirs})


@api_view(['GET'])
def create_catalog(request):
    catalog_name = request.GET.get('catalog_name')
    if not os.path.exists(ROOT_PATH+catalog_name):
        os.makedirs(ROOT_PATH+catalog_name)
        return Response("OK")
    return Response("Already exist")


@api_view(['GET'])
def rename_catalog(request):
    catalog_name = request.GET.get('catalog_name')
    new_name = request.GET.get('new_name')

    if os.path.exists(ROOT_PATH + catalog_name):
        os.rename(ROOT_PATH + catalog_name,ROOT_PATH + new_name)
        return Response("OK")
    return Response("Doesn't exist")

# @api_view(['GET'])
# def delete_catalog(request):
#     catalog_name = request.GET.get('catalog_name')
#     if os.path.exists(ROOT_PATH + catalog_name):
#
