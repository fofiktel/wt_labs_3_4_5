from django.contrib.postgres.search import SearchVector
from .serializers import NewsSerializer
from rest_framework import generics
from .models import News

class SearchAPIView(generics.ListAPIView):
    model = News
    serializer_class = NewsSerializer

    def get_queryset(self):
        data = self.request.GET.get('data')
        list = News.objects.annotate(
            search=SearchVector('title', 'article')).filter(search=data)
        return list
