import shutil

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
    name = request.GET.get('name')
    if not os.path.exists(ROOT_PATH + name):
        os.makedirs(ROOT_PATH + name)
        return Response("OK")
    return Response("Already exist")


@api_view(['GET'])
def rename_catalog(request):
    name = request.GET.get('name')
    new_name = request.GET.get('new_name')

    if os.path.exists(ROOT_PATH + name):
        os.rename(ROOT_PATH + name, ROOT_PATH + new_name)
        return Response("OK")
    return Response("Doesn't exist")

@api_view(['GET'])
def delete_catalog(request):
    name = request.GET.get('name')
    if os.path.exists(ROOT_PATH + name):
        shutil.rmtree(ROOT_PATH + name)
        return Response("OK")
    return Response("Doesn't exist")

@api_view(['GET'])
def copy_file(request):
    copy_from = ROOT_PATH + request.GET.get('from')
    copy_to = ROOT_PATH + request.GET.get('to')

    if os.path.exists(copy_from) and os.path.exists(copy_to):
        shutil.copy(copy_from, copy_to)
        return Response("OK")
    return Response("Doesn't exist")


@api_view(['GET'])
def read_file(request):
    name = request.GET.get('name')
    if os.path.exists(ROOT_PATH+name):
        with open(ROOT_PATH+name) as file:
            str = file.read()
        return Response(str)
    return Response("Doesn't exist")





