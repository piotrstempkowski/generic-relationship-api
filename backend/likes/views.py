from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .models import Like
from .serializers import LikeSerializer


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [TokenAuthentication]
    filter_backends = [OrderingFilter]
    ordering = ["id"]

    # def get_queryset(self):
    #     if self.request.user.is_staff:
    #         return self.queryset
    #     return self.queryset.filter(author=self.request.user)
    #
    # def perform_create(self, serializer):
    #     return serializer.save(author=self.request.user)

# Create your views here.
