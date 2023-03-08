from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserCreateSerializer, UserReadSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated


class ReadCreateOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in ('GET', 'HEAD', 'OPTIONS', 'POST')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated|ReadCreateOnly]

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return UserReadSerializer
        return UserCreateSerializer
