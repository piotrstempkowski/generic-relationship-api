from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializer
from .models import Blog
from rest_framework.viewsets import ModelViewSet

from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # authentication_classes = [TokenAuthentication]

# Create your views here.
