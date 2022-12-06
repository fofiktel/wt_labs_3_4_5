import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cryptography.fernet import Fernet
from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User

KEY = b'raTleA9iB8Nl4-hQb4wn7LYU_i909VCHfT50GFVcfdk='


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def encrypt(request):
    data = request.GET.get('data')
    f = Fernet(KEY)
    dec_data = f.decrypt(data).decode()
    print(type(json.dumps(json.loads(dec_data))))
    return Response(json.loads(dec_data))

