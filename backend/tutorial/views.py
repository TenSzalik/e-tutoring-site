from rest_framework.viewsets import ModelViewSet
from backend.viewsets import ReadApiView
from .models import Tutorial, Language
from .serializers import TutorialReadSerializer, TutorialCreateUpdateSerializer, LanguageSerializer
from django_filters import rest_framework as filters


class LanguageViewSet(ReadApiView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class TutorialFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Tutorial
        fields = ["lvl", "homework", "place", "support_disabled", "language"]


class TutorialViewSet(ModelViewSet):
    queryset = Tutorial.objects.all()
    filterset_class = TutorialFilter

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return TutorialReadSerializer
        return TutorialCreateUpdateSerializer

    def perform_create(self, serializer):
        data = {"created_by": self.request.user}
        return serializer.save(**data)

    def perform_update(self, serializer):
        created_by = {"created_by": self.request.user}
        data = dict(created_by)
        return serializer.save(**data)
